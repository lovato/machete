# -*- coding: UTF-8 -*-
from machete import __version__, log
import shutil
import errno
import os
import subprocess

is_chicken = False


def os_call(path):
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
    path = os.path.abspath(os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "../templates"))
    base_path = os.path.join(path, "_base")
    template_path = os.path.join(path, template)

    base_files = os.listdir(base_path)
    template_files = os.listdir(template_path)

    # check for empty dir first, else abort

    for each in base_files:
        copyanything(os.path.join(base_path, each), os.path.join(".", each))
    for each in template_files:
        copyanything(os.path.join(template_path, each),
                     os.path.join(".", each))


def git_init():
    if not is_chicken:
        try:
            os_call('git init')
        except:
            pass  # thats ok, you can sort of live without git


def rename_files(project):
    if not is_chicken:
        shutil.move('packagesample', project)
        shutil.move('docs/example/packagesample.cfg',
                    'docs/example/' + project + '.cfg')


def perform_replaces(project):
    if not is_chicken:
        files = ['setup.py', 'README.md', 'run.py', 'MANIFEST.in',
                 'docs/source/changelog.rst', project+'/start.py',
                 project+'/__init__.py', project+'/submodule/module.py',
                 project+'/submodule/__init__.py', 'tests/test_version.py',
                 'setup.cfg']
        for each in files:
            replace_infile('packagesample', project, each)


def has_virtualenv():
    try:
        return 'Usage' in os_call('virtualenv --help')
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


def create_env(project):
    if not is_chicken:
        if has_virtualenvwrapper():
            os_call('mkvirtualenv --clear '+project)
        else:
            if has_virtualenv():
                os_call('virtualenv .venv_'+project+'')

        if has_virtualenv():
            if os.path.isfile('requirements.txt'):
                os_call('pip install -r requirements.txt')
            if os.path.isfile('requirements-dev.txt'):
                os_call('pip install -r requirements-dev.txt')


def main(template, project, chicken):
    global is_chicken
    is_chicken = chicken
    if is_chicken:
        print('RUNNING ON CHICKEN MODE')
    # check for complete empty dir first, else abort

    git_init()
    copy_files(template)
    rename_files(project)
    perform_replaces(project)
    create_venv(project)
