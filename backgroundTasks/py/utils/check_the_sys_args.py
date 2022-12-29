import os, sys

def check_the_sys_args():

    mode = sys.argv[1]
    list_of_acceptable_args = ['dev', 'run']
    if not mode in list_of_acceptable_args:
        raise ValueError (
            "The passed arg after main.py must to be one of " + \
            f"{list_of_acceptable_args}"
        )
    os.environ['MODE'] = mode