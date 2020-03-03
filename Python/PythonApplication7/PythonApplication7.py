def gettext():
    txt=open("1.txt",'r').read()
    txt=txt.lower()
    for ch in "!@#$%^&*()_+''"".;][|?><:~":
        txt=txt.replace(ch,' ')
    return txt

t1=gettext()
words=t1.split()
counts={}
for i in words:
    counts[i]=counts.get(i,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in items:
    print(i)