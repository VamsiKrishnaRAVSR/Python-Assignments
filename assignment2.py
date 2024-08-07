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

# 2 methods, 
# Using the 2 loops which doesn't require additional space(O(1)) but time complexity will be O(n^2)
# using the single loop but we need to create another variable(O(word_size)) but tume complexity is O(n)
def checkRepeatedChars(word):
    newWord = ''
    isFound=False
    for i in word:
        if i in newWord:
            isFound=True
            break
        else:
            newWord+=i
    if(isFound):
        print(F"{word} has repeated characters")
    else:
        print(F"{word} has all unique words")

checkRepeatedChars('aab')
checkRepeatedChars('def')
checkRepeatedChars('abc')


# Function
# Convert all the above to function which can work on variadic number of arguments

# Palindrome
def multipleParamFunctions(*args):
    for word in args:
        reverse_word = word[::-1]
        if(word==reverse_word): 
            print(F"{word} is a palindrome")
        else:
            print(F"{word} is not a palindrome")

multipleParamFunctions("abc", "def", "aba")

# Multiple characters
def checkRepeatedCharsMultiple(*words):
    for word in words:
        newWord = ''
        isFound=False
        for i in word:
            if i in newWord:
                isFound=True
                break
            else:
                newWord+=i
        if(isFound):
            print(F"{word} has repeated characters")
        else:
            print(F"{word} has all unique words")
checkRepeatedCharsMultiple('aab', "def")

