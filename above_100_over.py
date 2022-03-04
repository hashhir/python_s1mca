l=list(map(int,input("enter a list of numbers").split()))
for i in l:
    if i>100:
        l[l.index(i)]='over'
print(*l,sep=',')
