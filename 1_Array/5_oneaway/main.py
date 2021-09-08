#There are 3 types of edits that can be performed on a string: insert charecter, remove a charecter, replace a charecter.
#Given 2 strings, check if they are one edit or zero edit away
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bae -> false


#IF SAME LENGTH -> EDIT -> ONLY 1 DIFFERENT POSITION

#IF LEN STR 1 + 1 < LEN STR 2 -> FALSE 
#ELSE:  #str1 is substring is string 2 -> True #else false 

def one_edit(str1, str2):
    if str1[0] == str2[0]:
        num_diff = 0
        i = 0
        j = 0
        for c in str1:
            if str1[i] == str2[j]:
                i += 1
                j += 1
            else:
                if num_diff == 1:
                    return False
                else:
                    i += 1
                    j += 2
        return True
    elif str1[0] == str2[1]:
        for i in range(len(str1)):
            if str1[i] != str2[i+1]:
                return False
        return True
    else:
        return False


def one_replace(str1, str2):
    diff = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            diff +=1

    if diff > 1:
        return False
    else:
        return True 

def oneway(str1, str2):
    if len(str1) == len(str2):
        return one_replace(str1, str2)
    elif len(str1) + 1 == len(str2):
        return one_edit(str1, str2)
    elif len(str1) - 1 == len(str2):
        return one_edit(str2, str1)
    else:
        return False

def main():
    str1 = input("Str1: ")
    str2 = input("Str2: ")

    ans = oneway(str1, str2)
    print(ans)

if __name__ == "__main__":
    main()