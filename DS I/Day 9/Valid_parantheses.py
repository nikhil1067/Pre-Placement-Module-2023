class Solution:
    def isValid(self, s: str) -> bool:
        valid=["()","{}","[]"]
        count=0
        for i in valid:
            if i in s:
                s=s.replace(i, "")
                count+=1
        if s=="":
            return True
        elif s!="" and count==0:
            return False
        else:
            return self.isValid(s)
        