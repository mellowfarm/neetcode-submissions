class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        res = []
        for i in range(len(strs)):
            original = strs[i]
            sort = "".join(sorted(original))
            if sort in anagrams:
                anagrams[sort].append(original)
            else:
                anagrams[sort] = [original]
        for key, value in anagrams.items():
            res.append(value)
        return res