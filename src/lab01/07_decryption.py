trash="thisisabracadabraHt1eadljjl12ojh."
clear=""
n1=0
n2=0
for f in trash:
    n1+=1
    if f.isupper():
        clear+=f
        break
for d in trash:
    n2+=1
    if d.isdigit():
        break
progress=clear
m=n2-n1
c=0
for i in trash[n1:]:
    c+=1
    if c%(m+1)==0:
        progress+=i
    if i==".":
        break
print(progress)