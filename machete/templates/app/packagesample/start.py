# -*- coding: utf-8 -*-
# pep8: disable-msg=E501
# pylint: disable=C0301

from packagesample import __version__, log, modules
import argparse
import __builtin__


def main():
    log.info("packagesample v" + __version__)
    parser = argparse.ArgumentParser(
        description='packagesample v' + __version__)

    parser.add_argument(
        '-x', '--xunxo', help='Sample NonRequired Parameter', required=False)

    tasks = modules.__all__

    try:
        if len(tasks) > 1:
            tasks_str = ', '.join(tasks)
            k = tasks_str.rfind(",")
            tasks_str = tasks_str[:k] + " or" + tasks_str[k + 1:]
        else:
            tasks_str = tasks[0]

        parser.add_argument(
            '-t', '--task',
            help='Task to be performed. Allowed values: ' + tasks_str + '.',
            metavar='<task_name>',
            choices=tasks,
            required=True)
    except:
        pass

    parser.add_argument(
        "--chicken",
        help="Chicken mode (optional). Does NOT CHANGE anything.",
        action="store_true")

    args = parser.parse_args()  # if required params arent met, program aborts
    __builtin__.chicken = args.chicken

    try:
        result = eval(args.task + '.main()')
        result = 'RESULT for "' + args.task + '" = ' + result
        log.debug(result)
        exit(0)
    except Exception as e:
        import traceback
        log.error(traceback.format_exc())
        exit(1)
