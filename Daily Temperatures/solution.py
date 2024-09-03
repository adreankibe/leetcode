class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize the result list with zeros, same length as temperatures
        res = [0] * len(temperatures)
        # Initialize an empty stack to keep track of temperatures and their indices
        stack = []

        # Iterate over the list of temperatures with their indices
        for i, t in enumerate(temperatures):
            # While stack is not empty and the current temperature is greater than the temperature at the top of the stack
            while stack and t > stack[-1][0]:
                # Pop the top element from the stack
                stackT, stackInd = stack.pop()
                # Calculate the number of days until a warmer temperature and store it in the result list
                res[stackInd] = (i - stackInd)
            # Push the current temperature and its index onto the stack
            stack.append([t, i])
        
        # Return the result list
        return res