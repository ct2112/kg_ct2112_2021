import sys

def isInlist(inp, skip):

    for i in skip:
        if i == inp:
            return True
    return False 

def isonetoone(st1, st2):
     #  1. check if you are the same as anyone later, 
     #  2. if they are, then the corresponding in str2 must be the same as well
   

    if len(st1) != len(st2):
        print("Strings are not the same length")
        return False
    
    # contains values of positions already checked because they match a previous char
    skip_check = []

    for i in range(len(st2)):
        if isInlist(i, skip_check):
            continue

        for j in range(i+1,len(st2)):
            if st1[i] == st1[j]:
                if st2[i] != st2[j]:
                    return False
                else:
                    skip_check.append(j)

    return True
