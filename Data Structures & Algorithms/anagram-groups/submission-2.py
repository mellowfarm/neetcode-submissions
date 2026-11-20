class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen = {}
        res = []

        for string in strs:
            key = str(sorted(string))
            if key in seen:
                seen[key].append(string)
            else:
                seen[key] = [string]
        
        for k, v in seen.items():
            res.append(v)
        
        return res

        

