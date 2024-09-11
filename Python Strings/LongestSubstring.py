"""
### 3. **Longest Substring Without Repeating Characters**
Given a string, find the length of the longest substring without repeating characters.
- **Input**: A string
- **Output**: The length of the longest substring without repeating characters.

"""
def length_of_longest_substring(s):
    # Dictionary to store the last index of each character
    char_index = {}
    max_length = 0
    start = 0  # Starting index of the current substring

    # Iterate through the string
    for i, char in enumerate(s):
        # If the character is found in the dictionary and is within the current substring
        if char in char_index and char_index[char] >= start:
            # Move the start to one position after the last occurrence of the character
            start = char_index[char] + 1
        
        # Update the character's last index
        char_index[char] = i
        
        # Calculate the length of the current substring and update max_length if it's longer
        max_length = max(max_length, i - start + 1)

    return max_length

# Example usage:
string = "abcabcbb"
print(f"Length of the longest substring without repeating characters: {length_of_longest_substring(string)}")
