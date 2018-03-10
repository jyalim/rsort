#!/usr/bin/env python
import natsort
import glob
import collections
import sys
"""
  NOTE: This program essentially assumes it is working with FILENAMES

  TODO: type/error checking and generality
  TODO: take options 
          - allow reversal
          - allow different natsort procedures
          - filename mode -- allow sort on basenames only
          - general mode (no globbing)
"""

def flatten_list(_list):
  """
    From: https://stackoverflow.com/questions/2158395/flatten-an-irregular-list-of-lists
  """
  for sub_list in _list:
    obj_iterable = isinstance(sub_list,collections.Iterable)
    obj_str_bytes= isinstance(sub_list,(str,bytes))
    if obj_iterable and not obj_str_bytes:
      yield from flatten_list(sub_list)
    else:
      yield sub_list

def main(args):
  strs = []
  for arg in args:
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
  args = sys.argv[1:]
  s    = main(args) 
