class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)  # Calculate the total sum of all elements in the list
        left_sum = 0  # Initialize the left sum to 0
        
        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]  # Calculate the right sum by subtracting the left sum and the current element from the total sum
            
            if left_sum == right_sum:  # If the left sum is equal to the right sum, we have found the pivot index
                return i
            
            left_sum += nums[i]  # Add the current element to the left sum
            
        return -1  # If no pivot index is found, return -1
