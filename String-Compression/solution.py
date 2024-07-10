class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # Initialize two pointers, read and write, to keep track of the current position in the list
        read, write = 0, 0

        # Iterate through the list until the read pointer reaches the end
        while read < len(chars):
            # Store the current character in a variable
            currentChar = chars[read]
            # Initialize a variable to keep track of the count of consecutive characters
            charCount = 0

            # Count the number of consecutive occurrences of the current character
            while read < len(chars) and chars[read] == currentChar:
                read += 1
                charCount += 1

            # Write the current character to the write position in the list
            chars[write] = currentChar
            write += 1

            # If the count of consecutive characters is greater than 1, write the count as individual digits
            if charCount > 1:
                for digit in str(charCount):
                    chars[write] = digit
                    write += 1

        # Return the write pointer, which represents the length of the compressed list
        return write