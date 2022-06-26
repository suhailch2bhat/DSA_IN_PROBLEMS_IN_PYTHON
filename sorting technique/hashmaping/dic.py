print("Hello world")
a=[1,3,3,4,1,6,9]
d={}
for i in a:
    if i in d:
        d[i]=d[i]+112
    else:
        d[i]=1
print(d,"dic")
mx=max(d.values())
print(mx,"max")
mi=min(d.values())
print(mi,"min")
for key,value in d.items():
    print(key,"key")
    print(value,"value")
word=["apple","spd","jkl","werweasd"]
word.sort(key=lambda x:len(x),reverse=True)
print(word,"sort on base of lenght")
