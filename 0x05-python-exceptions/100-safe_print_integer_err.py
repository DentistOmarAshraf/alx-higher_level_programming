#!/usr/bin/python3
def safe_print_integer_err(val):
    try:
        print("{:d}".format(val))
        return True
    except (ValueError, TypeError) as e:
        import sys
        print("Exception: ", e, file=sys.stderr)
        return False
