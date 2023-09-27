class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        total_length = 0

        # Calculate the total length of the decoded string
        for char in s:
            if char.isdigit():
                total_length *= int(char)
            else:
                total_length += 1

        # Traverse the string in reverse to find the character at index k
        for char in reversed(s):
            k %= total_length  # Reduce index based on the length

            # Check if the current character is the answer
            if k == 0 and char.isalpha():
                return char

            # Update the length based on the current character
            if char.isdigit():
                total_length //= int(char)
            else:
                total_length -= 1