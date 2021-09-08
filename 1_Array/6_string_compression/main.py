#perform basic string compression using the counts of repeated characters
# for exp, aabccccaaa -> a2b1c5a3
# if the compressed string has bigger length than the origional string -> return original string 
# ASSUME: string only has lower case and upper case character


str1 = input(str)

def compress_string(str1):
    for c in str1:
        pass