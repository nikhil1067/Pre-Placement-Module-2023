from math import log
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n and not(n & n-1)