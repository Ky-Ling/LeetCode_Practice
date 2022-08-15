from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # (1): Sort each of them : m * O(nlogn) --> m is the length of strs, n is the length of each element


        # (2): HashMap: key -> 1a, 1e, 1t; value:["eat", "ate", "tea"] --> list of anagram
        #  O(m * n * 2) -> m is the length of strs, n is the length of each element
        
        # Mapping charCount in each string to list of anagrams

        res = defaultdict(list)

        for s in strs:
            # From a -> z
            count = [0] * 26

            # Go through each character in the str:
            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return res.values()


s = Solution()

print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(s.groupAnagrams([""]))
print(s.groupAnagrams(["a"]))


