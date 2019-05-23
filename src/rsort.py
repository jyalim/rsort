#!/usr/bin/env python
import natsort
import glob
from collections.abc import Iterable
import sys
"""
  VERSION: 0.1.0
  NOTE: This program essentially assumes it is working with FILENAMES

  TODO: type/error checking and generality
  TODO: take options 
          - allow different natsort procedures
          - filename mode -- allow sort on basenames only
          - general mode (no globbing)
          - appropriate stdin mode
            + treat strings literally 
  TODO: Modularity
"""
def parse_args():
  args = []
  try:
    if len(sys.argv) > 1:
      for arg in sys.argv[1:]:
        args.append(arg)
    if not sys.stdin.isatty():
      for line in sys.stdin.readlines():
        args.append(line.rstrip('\n'))
    if len(args) <= 1:
      print(args[0])
      print('ERROR -- 1 or fewer strings passed to sort')
      sys.exit(1)
  except Exception as ex:
    print('ERROR -- ',ex)
  return args

def flatten_list(_list):
  """
    From: https://stackoverflow.com/questions/2158395/flatten-an-irregular-list-of-lists
  """
  for sub_list in _list:
    obj_iterable = isinstance(sub_list,Iterable)
    obj_str_bytes= isinstance(sub_list,(str,bytes))
    if obj_iterable and not obj_str_bytes:
      yield from flatten_list(sub_list)
    else:
      yield sub_list

def rsort(strings_to_sort):
  strs = []
  for arg in strings_to_sort:
    if '*' in arg:
      res = glob.glob(arg)
    else:
      # TODO: check if file
      res = arg
    strs.append(res)
  strs = natsort.realsorted(flatten_list(strs))

  for string in strs:
    print(string)
  
  return strs

if __name__ == '__main__':
  args = parse_args()
  s    = rsort(args) 
