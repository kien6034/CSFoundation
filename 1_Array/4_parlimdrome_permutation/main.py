#given a string, write a function to check if that string is a permuatation of a palindrome
#a palindrome is a word or phrase that is the same forwards and backwords

not_alphabet = [" ", "/", "/n", "/t"]

def count_freq(str1):
    freq = dict()

    for x in str1:
        if x in not_alphabet:
            continue
        freq[x] = 0

    for x in str1:
        if x in not_alphabet:
            continue
        freq[x] +=1
    
    return freq

def check_parlimdrome(freq):
    odd_nums = 0
    total = 0
    for k in freq:
        total += freq[k]
        if freq[k] % 2 == 1:
            odd_nums +=1
    
    if odd_nums > 1:
        return False
    elif odd_nums == 1:
        if total % 2 == 0:
            return False 
        else:
            return True 
    else:
        return True


str1 = input("enter your string: ")
freq = count_freq(str1)
print(freq)
ans = check_parlimdrome(freq)
print(ans)