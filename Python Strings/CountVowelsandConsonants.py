"""
### 5. **Count Vowels and Consonants**
Write a Python program to count the number of vowels and consonants in a given string. You should ignore case and non-alphabetic characters.
- **Input**: A string
- **Output**: Two integers, the number of vowels and the number of consonants.

These problems will help strengthen your understanding of string manipulation in Python!

"""

def count_vowels_and_consonants(s):
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    consonant_count = 0
    
    # Iterate through each character in the string
    for char in s:
        # Check if the character is alphabetic
        if char.isalpha():
            # Check if the character is a vowel
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return vowel_count, consonant_count

# Example usage:
string = "Hello, World! 123"
vowels, consonants = count_vowels_and_consonants(string)
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
