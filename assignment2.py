# Slicing
# Get element from second position to fifth position from list - [1, 2, 3, 4, 5, 6]

arr = [1, 2, 3, 4, 5, 6]
print(arr[2:6])

# Condition
# Check if string palindrome or not “ab”, “abc”, “aba”

def isPalindrome(word):
    reverse_word = word[::-1]
    if(word==reverse_word): 
        print(F"{word} is a palindrome")
    else:
        print(F"{word} is not a palindrome")
isPalindrome('ab')
isPalindrome('abc')
isPalindrome("aba")

# Loop
# Check if string contains repeated characters “aab”, “abc”, “def”

def checkRepeatedChars(word):
    wordSet=set(word)
    if(len(word) == len(wordSet)):
        print(F"{word} has all unique words")
    else: 
        print(F"{word} has repeated characters")
checkRepeatedChars('aab')
checkRepeatedChars('def')
checkRepeatedChars('abc')

def multipleParamFunctions(*args):
    for word in args:
        reverse_word = word[::-1]
        if(word==reverse_word): 
            print(F"{word} is a palindrome")
        else:
            print(F"{word} is not a palindrome")


multipleParamFunctions("abc", "def", "aba")