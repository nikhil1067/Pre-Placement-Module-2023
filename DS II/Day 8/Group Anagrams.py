from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dd=defaultdict(list)
        for i in strs:
            ss="".join(sorted(i))
            dd[ss].append(i)
        return dd.values()
