n=int(input())
t=0
f=0
i=0
while i<n:
    m=(input(f"in_{i+1}:"))
    if m.split()[0].isalpha() and m.split()[1].isalpha() and m.split()[2].isdigit():
        if m.split()[-1]=="True":
            t+=1
            i+=1
        elif m.split()[-1]=="False":
            f+=1
            i+=1
    else:
        print("Ваша запись не соответствует формату! Попробуйте еще раз.")
print("out: ",t,f)