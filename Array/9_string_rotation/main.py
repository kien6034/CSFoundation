#assume that you have a method isSubstring which checks one word is a substring of another
#given 2 strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call isSubstring


str1 = input("enter string 1: ")
str2 = input("enter string 2: ")

def isRotation(str1, str2):
    if len(str1) != len(str2):
        return False
        

    str3 = str2 + str2
  
    if str1 in str3:
        return True
    else:
        return False

if isRotation(str1, str2):
    print("YEs")
else:
    print("No")