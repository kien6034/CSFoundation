#Write a method to replace all spaces in a string with "%20"

#Assuming that string has sufficent space at the end to hold additonal characters, and you're given the true length of string 


def countSpace(str):
    spaceNum = 1
    for c in str:
        if c == " ":
            spaceNum +=1
    
    return spaceNum

def urlify(str, spaceNum):
    new_string = ""
    print(len(str))
    for i in reversed(range(len(str) + spaceNum*3)):
        pass

    return new_string

str = input("enter string: ")
spaceNum = countSpace(str)
urlify_string = urlify(str, spaceNum)