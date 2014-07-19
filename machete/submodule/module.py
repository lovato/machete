# -*- coding: UTF-8 -*-
from machete import __version__, log
import shutil
import errno
import os
import subprocess

is_chicken = False


def os_call(path):
    log.debug(path)
    proc = subprocess.Popen(path.split(' '), stdout=subprocess.PIPE)
    (out, err) = proc.communicate()
    return out


def replace_infile(lookfor, replace, text_file):
    try:
        infile = open(text_file)
        outfile = open(text_file+'.tmp', 'w')

        # replacements = {'zero':'0', 'temp':'bob', 'garbage':'nothing'}
        replacements = {lookfor: replace}

        for line in infile:
            for src, target in replacements.iteritems():
                line = line.replace(src, target)
            outfile.write(line)
        infile.close()
        outfile.close()
        shutil.move(text_file+'.tmp', text_file)
        return True
    except:
        return False


def copyanything(src, dst):
    if 'egg-info' in src:
        return True
    if 'dist' in src:
        return True
    if not is_chicken:
        try:
            shutil.copytree(src, dst)
        except OSError as exc:  # python >2.5
            if exc.errno == errno.ENOTDIR:
                shutil.copy(src, dst)
            else:
                raise
    else:
        print('copy from '+src.split('machete')[2]+' to '+dst)


def copy_files(template):
    print ("Copying files from template...")
    try:
        if not is_chicken:
            path = os.path.abspath(os.path.join(
                os.path.dirname(os.path.realpath(__file__)), "../templates"))
            print path
            base_path = os.path.join(path, "_base")
            template_path = os.path.join(path, template)

            base_files = os.listdir(base_path)
            template_files = os.listdir(template_path)

            for each in base_files:
                copyanything(
                    os.path.join(base_path, each), os.path.join(".", each))
            for each in template_files:
                copyanything(os.path.join(template_path, each),
                             os.path.join(".", each))
        return True
    except:
        return False


def git_init():
    print ("Initializing GIT...")
    if not is_chicken:
        try:
            os_call('git init')
        except:
            pass  # thats ok, you can sort of live without git


def rename_files(project):
    print ("Modifying copied files names...")
    try:
        if not is_chicken:
            shutil.move('packagesample', project)
            shutil.move('docs/example/packagesample.cfg',
                        'docs/example/' + project + '.cfg')
        return True
    except:
        return False


def perform_replaces(project):
    print ("Modifying copied files content...")
    try:
        if not is_chicken:
            files = ['setup.py', 'README.md', 'run.py', 'MANIFEST.in',
                     'docs/source/changelog.rst', project+'/start.py',
                     project+'/__init__.py', project+'/submodule/module.py',
                     project+'/submodule/__init__.py', 'tests/test_version.py',
                     'setup.cfg']
            for each in files:
                replace_infile('packagesample', project, each)
        return True
    except:
        return False


def has_virtualenv():
    try:
        return 'Usage' in os_call('virtualenv')
    except:
        return False


def has_virtualenvwrapper():
    if has_virtualenv():
        try:
            # only works on linux
            return '/usr' in os_call('which virtualenvwrapper.sh')
        except:
            return False
    else:
        return False


def create_venv(project):
    print ("Creating virtualenv...")
    try:
        if not is_chicken:
            log.debug('Trying to create virtualenv')
            env_path = os.getenv('WORKON_HOME', './.venv_')
            full_env_path = env_path
            if has_virtualenvwrapper():
                full_env_path = os.path.join(env_path, project)
                os_call('virtualenv --clear ' + full_env_path)
            else:
                if has_virtualenv():
                    full_env_path = os.path.join(env_path + project)
                    os_call('virtualenv ' + full_env_path)

            print ("\nSUCCESS!!!")

            activate = full_env_path + '/bin/activate'
            if os.path.isfile(activate):
                print("Please execute 'source " + activate + "' to enter into your virtualenv")
                #http://stackoverflow.com/questions/6943208/activate-a-virtualenv-with-a-python-script

                if has_virtualenv():
                    if os.path.isfile('requirements.txt'):
                        print("Then please execute 'pip install -r requirements.txt'")
                        # os_call('pip install -r requirements.txt')
                    if os.path.isfile('requirements-dev.txt'):
                        print("And after please execute 'pip install -r requirements-dev.txt'")
                        # os_call('pip install -r requirements-dev.txt')
        return True
    except:
        return False


def main(template, chicken):
    global is_chicken
    is_chicken = chicken
    if is_chicken:
        log.debug('RUNNING ON CHICKEN MODE')
        print('*** RUNNING ON CHICKEN MODE ***')

    if os.listdir('.'):
        message = 'Current directory is not empty, so machete cannot run :-('
        log.warn(message)
        print(message)
        exit(0)

    project = os.path.basename(os.getcwd()).replace('-', '_')
    git_init()
    if copy_files(template):
        if rename_files(project):
            if perform_replaces(project):
                if create_venv(project):
                    print ('\nmachete says: "Its done!"')
