#!/usr/bin/python

####################
# Author : Siqi Chen
# Date : 2018-04-02
# Work : REDUCER - NYC Traffic
####################

import sys
# from collections import defaultdict


def reducer(lines):

    current_count = 0
    current_type = None
    type_ = None

    for line in lines:

        line = line.strip()
        type_, count = line.split('\t', 1)

        type_ = str(type_).upper()

        try:
            count = int(count)
        except ValueError:
            continue

        if current_type == type_:
            current_count += count
        else:
            if current_type:
                print '%s\t%s' % (current_type, current_count)
            current_count = count
            current_type = type_

    if current_type == type_:
        print '%s\t%s' % (current_type, current_count)


# main() calls the reducer function
def main():
    lines = sys.stdin.readlines()
    reducer(lines)


if __name__ == '__main__':
    main()
