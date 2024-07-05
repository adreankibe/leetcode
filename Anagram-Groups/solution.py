from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary to store the anagram groups
        res = defaultdict(list)

        # Iterate through each string in the input list
        for s in strs:
            # Create a list to store the count of each character in the string
            count = [0] * 26

            # Iterate through each character in the string
            for c in s:
                # Increment the count of the character by 1
                count[ord(c) - ord("a")] += 1

            # Convert the count list to a tuple and use it as a key in the dictionary
            # Append the string to the list of values corresponding to the key
            res[tuple(count)].append(s)

        # Return the values of the dictionary, which are the grouped anagrams
        return res.values()