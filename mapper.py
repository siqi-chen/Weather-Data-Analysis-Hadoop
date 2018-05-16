#!/usr/bin/python

####################
# Author : Siqi Chen
# Date : 2018-04-02
# Work : MAPPER - NYC Traffic
####################

import sys
# import csv
# from StringIO import StringIO  # python2.7
# import io
import re


def mapper(lines):

    for line in lines:

        # #--- remove leading and trailing whitespace---
        line = line.strip()
        # record = line.split(',')
        record = re.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", line)
        # object_line = csv.reader(io.StringIO(line))  # , skipinitialspace=True)
        # object_line = csv.reader(StringIO(line))  # python2.7
        # record = object_line.next()

        if len(record) == 29 and record[0] != 'DATE':

            five_vehicles = record[-5:]

            for vehicle in five_vehicles:
                if vehicle != '':
                    print '%s\t%s' % (str(vehicle), 1)
                else:
                    print '%s\t%s' % ('None', 1)


# main() calls the mapper function
def main():
    lines = sys.stdin.readlines()
    # lines = open('test.txt', 'r')
    mapper(lines)


if __name__ == '__main__':
    main()
