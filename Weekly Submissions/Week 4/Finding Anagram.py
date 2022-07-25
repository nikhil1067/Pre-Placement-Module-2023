string1=input()
string2=input()
if sorted(string1)==sorted(string2):
    print("Valid Anagram")
else:
    print("Invalid Anagram")