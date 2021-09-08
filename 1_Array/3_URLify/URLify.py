#Write a method to replace all spaces in a string with "%20"

#Assuming that string has sufficent space at the end to hold additonal characters, and you're given the true length of string 


def countSpace(str):
    spaceNum = 0
    for c in str:
        if c == " ":
            spaceNum +=1
    
    return spaceNum

def convert(sequence):
    str = ""
    for x in sequence:
        str +=x 

    return str

def urlify(str, spaceNum):
    
    index = len(str) + spaceNum * 2
    new_string = []
    new_string = [0 for i in range(index)]

    for i in reversed(range(len(str))):
        if str[i] == " ":
            new_string[index - 1] = '0'
            new_string[index - 2] = '2'
            new_string[index - 3] = '%'
            index = index - 3
        else:
            new_string[index - 1] = str[i]
            index -= 1

    return new_string

str = input("enter string: ")
spaceNum = countSpace(str)
sequence = urlify(str, spaceNum)

urlify_string = convert(sequence)
print(urlify_string)