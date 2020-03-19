def isInlist(inp, skip):
    for i in skip:
        if i == inp:
            return True
    return False 

def isonetoone(st1, st2):
    # Cannot have a one to one map if lengths are different
    if len(st1) != len(st2):
        print("Strings are not the same length")
        return False
    
    already_checked = {}

    #  If the letter has been seen already in st1, check if the corresponding st2 values are the same
    for i in range(len(st1)):
        if st1[i] in already_checked: #if this is a duplicate
            if already_checked[st1[i]] != st2[i]:
                return False
        else:  
            already_checked[st1[i]] = st2[i]

    return True
