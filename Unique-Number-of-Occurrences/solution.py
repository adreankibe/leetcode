class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        # Create an empty dictionary to store the count of each number
        count_map = {}

        # Iterate through each number in the input array
        for num in arr:
            # Check if the number is already in the count_map
            if num in count_map:
                # If it is, increment the count by 1
                count_map[num] += 1
            else:
                # If it is not, initialize the count to 1
                count_map[num] = 1
        
        # Create an empty set to store the unique occurrences
        occurences = set()
        
        # Iterate through each count in the count_map
        for count in count_map.values():
            # Check if the count is already in the occurences set
            if count in occurences:
                # If it is, return False (not unique occurrences)
                return False
            else:
                # If it is not, add the count to the occurences set
                occurences.add(count)
        
        # If all counts are unique, return True
        return True