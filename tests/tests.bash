# test 1

TRAPPED=100

trapped() {
  echo "TRAPPED -- quitting"
  exit $TRAPPED
}

trap trapped 1 2 3 4 5 6 7 8

logger() {
  mesg="$1"
  python -c "hdr,ftr=72*'=',72*'-'; print('{:s}\n${mesg}\n{:s}'.format(hdr,ftr))"
}

t1() {
  # TO PASS: all files in root directory are printed and sorted
  logger "--  test 1 -- single glob arg"
  rsort "../*" 
}

t2() {
  # TO PASS: all files in root directory and test directory are printed
  #          and sorted
  logger "--  test 2 -- multiple glob args"
  rsort "../*" "*"
}

t3() {
  # TO PASS: string1 is output (not character grinded)
  logger "--  test 3 -- no glob, single arg"
  rsort "string1" 
}

t4() {
  # TO PASS: string1-3 are output and sorted
  logger "--  test 4 -- no glob, multiple args"
  rsort "string1" "string3" "string2"
}

t5() {
  # TO PASS: t1 and t4 results are passed simultaneously
  logger "--  test 5 -- single glob, two non glob arg"
  rsort "../*" "string1" "string3" "string2"
}

t6() {
  # TO PASS: t5 must pass
  logger "--  test 6 -- single glob, two non glob arg, pipe"
  echo -e "../*\nstring1\nstring3\nstring2" | rsort
}

t1
t2
t3
t4
t5
t6
