class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        
        def r(picked, total, candidates,target):
            result = []
            if total==target:
                return [picked]
            elif total>target:
                return False
            else:
                for i in range(len(candidates)):
                    c = candidates[i]
                    minus_result = r(picked+[c], total+c, candidates[i:],target)
                    if minus_result==False:
                        break
                    else:
                        result += minus_result
                return result
        
        return r([], 0, candidates,target)