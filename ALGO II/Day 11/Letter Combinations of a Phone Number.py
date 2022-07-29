class Solution:
    m = {
        2: 'abc',
        3: 'def',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'pqrs',
        8: 'tuv',
        9: 'wxyz'
    }
    
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        a = []
        
        first = digits[:1]
        rest = digits[1:]
        
        letters = self.m[int(first)]
        
        for i in letters:
            v = self.recur(i, rest)
            a += v
        
        return a
            
    def recur(self, combo, digits):
        if not digits:
            return [combo]
        
        first = digits[:1]
        rest = digits[1:]
        
        dial_letters = self.m[int(first)]
        
        a = []
        
        for i in dial_letters:
            v = self.recur(f'{combo}{i}', rest)
            a += v
        
        return a