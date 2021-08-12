'''s="lets reverse this string"
for i in range(len(s)-1,-1,-1):
    c=s[i]
    print(c,"")
'''
'''
s1="this is first string"
s2="This is second string"
s3="thisis. thir. dstring"
s4="this is fourth string"
print(s1.count("first"))
print(s1.find("is"))
print(s1.index("is"))
print(s1.upper())
print(s2.lower())
print(s3.isalpha())
print(s4.isdigit())
s5=s2.replace("i","j")
print(s5)
print(s3.split('.'))    
'''
a="0o1234"
b=int(a,base=8)
print(b)
c=oct(b)
d=hex(b)
e=int(b)
print(c)
print(d)
print(e)
print(int(0o123))
print(int(b))