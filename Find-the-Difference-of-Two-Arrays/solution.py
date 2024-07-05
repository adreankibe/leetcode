class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """

        # Convert nums1 and nums2 into sets to remove duplicates
        set1 = set(nums1)
        set2 = set(nums2)

        # Find the elements that are in set1 but not in set2
        diff1 = list(set1 - set2)
        # Find the elements that are in set2 but not in set1
        diff2 = list(set2 - set1) 

        # Return the differences as a list of lists
        return [diff1, diff2]
    



