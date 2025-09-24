def xo(s):
    s = s.lower()
    

    return s.count(char1) == s.count(char2)

char1 = ('x')
char2 = ('o')
print(xo("xoox"))
print(xo("xooooxox"))
print(xo("xoxoxoxoxoxoooxox"))

#Exes and Ohs
#https://www.codewars.com/kata/55908aad6620c066bc00002a
    