#! /usr/bin/env python

# hitjim@gmail.com
# drive performance balance calculator
#
# usage guide:
# USE IT!!

import sys
import argparse
import collections

parser = argparse.Argument.Parser(description="""Enter the number of drives
    in a VG (r), Average IOs queued per drive (AQD),  
