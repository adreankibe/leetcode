class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []  # Create an empty stack to store opening parentheses
        curlyMap = {")": "(", "]": "[", "}": "{"}  # Create a mapping of closing parentheses to their corresponding opening parentheses
        
        for c in s:  # Iterate through each character in the input string
            if c in curlyMap:  # If the character is a closing parenthesis
                if stack and stack[-1] == curlyMap[c]:  # Check if the stack is not empty and the top element of the stack matches the corresponding opening parenthesis
                    stack.pop()  # If they match, remove the top element from the stack
                else:
                    return False  # If they don't match, return False as the parentheses are not valid
            else: 
                stack.append(c)  # If the character is an opening parenthesis, add it to the stack
        
        return True if not stack else False  # If the stack is empty, all parentheses are valid and return True. Otherwise, return False.