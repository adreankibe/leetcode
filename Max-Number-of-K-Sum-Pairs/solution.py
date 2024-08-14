class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        nums.sort()
        count = 0
        i = 0
        j = len(nums) -1

        while i < j:
            current_sum = nums[i] + nums[j]

            if current_sum == k:
                count += 1
                i += 1
                j -= 1
            
            elif current_sum < k:
                i += 1
            else:
                j -= 1
        return count
        