import sys

def isonetoone(st1, st2):
     #  1. check if you are the same as anyone later, 
     #  2. if they are, then the corresponding in str2 must be the same as well
   
    if len(st1) != len(st2):
        return False

    for i in range(len(st2)):
        for j in range(i,len(st2)):

            if st1[i] == st1[j]:
                if st2[i] != st2[j]:
                    return False
    return True




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