"""
### 2. **Anagram Detection**
Write a function to check if two strings are anagrams of each other. 
Two strings are anagrams if they contain the same characters with the same frequencies, but in a different order.

- **Input**: Two strings
- **Output**: Return `True` if the strings are anagrams, `False` otherwise.

"""

def are_anagrams(str1, str2):
    # Remove any spaces and convert both strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if the sorted characters of both strings are the same
    return sorted(str1) == sorted(str2)

# Example usage:
string1 = "Listen"
string2 = "Silent"

if are_anagrams(string1, string2):
    print(f'"{string1}" and "{string2}" are anagrams.')
else:
    print(f'"{string1}" and "{string2}" are not anagrams.')
