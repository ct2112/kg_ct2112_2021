import sys
from onetoone import *

def main():
    if len(sys.argv) != 3:
        print("Wrong Number of Arguments")
        return

    st1 = sys.argv[1]
    st2 = sys.argv[2]

    val = isonetoone(st1, st2)
    if val == 0:
      print("false")
    else:
      print("true")

main()