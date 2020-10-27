# palindromes w/out considering space and punctuation

import sys

def palindrome(word):
    if len(word) == 1:
        return True
    
    m = 0
    n = -1
    while m - n + 1 < len(word):
        if word[m] == word[n]:
            m += 1
            n -= 1
        else:
            return False
    return True


input = input("Enter word: ")
if palindrome(input.upper()) == True:
    print("True")
else:
    print("False")