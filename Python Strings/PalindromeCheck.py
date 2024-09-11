"""
### 1. **Palindrome Check**
Write a function that checks if a given string is a palindrome. A palindrome is a word, phrase, number, 
or other sequence of characters that reads the same forward and backward 
(ignoring spaces, punctuation, and capitalization).

- **Input**: A string
- **Output**: Return `True` if the string is a palindrome, `False` otherwise.

"""

def palindrome(Palindrome):


    print("Entered palindrome is: " + Palindrome)

    check = Palindrome[::-1]

    print("After Reverse: " + check)

    str1 = ''.join(char for char in check if check.isalnum())
    str2 = ''.join(char for char in Palindrome if Palindrome.isalnum())

    if str1.lower() == str2.lower():
        return 1
    else:
        return 0
        

if __name__ == "__main__":
    
    answer = palindrome(Palindrome = input("Enter a word, phrase or number: "))

    if answer == 1:
        print("It is Palindrome")
    else:
        print("Not Palindrome")
    
