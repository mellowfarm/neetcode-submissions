class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}
        res = []

        for string in strs:
            nstring = "".join(sorted(string))
            if nstring in anagram_groups:
                anagram_groups[nstring].append(string)
                continue
            anagram_groups[nstring] = [string]
        
        for key, value in anagram_groups.items():
            res.append(value)
        
        return res
