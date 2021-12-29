#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys
import os
import datetime

def main():
    v = sys.version_info
    print('Python version {}.{}.{}'.format(*v))
    p=sys.platform
    o=os.name
    e=os.getenv('PATH')
    now=datetime.datetime.now()


if __name__ == '__main__': main()
