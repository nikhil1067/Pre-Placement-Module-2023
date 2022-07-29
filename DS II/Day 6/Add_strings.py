class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def strtoint(s):
            num=0
            for i in s:
                num=(num*10)+(ord(i)-48)
            return num
        return str(strtoint(num1)+strtoint(num2))