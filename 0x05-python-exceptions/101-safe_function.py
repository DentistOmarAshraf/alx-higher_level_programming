#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        x = fct(*args)
        return x
    except (ValueError, ZeroDivisionError, IndexError, TypeError) as e:
        import sys
        print("Exception: {}".format(e), file=sys.stderr)
