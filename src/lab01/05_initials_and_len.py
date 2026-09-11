name=str(input("ФИО: "))
n1,n2,n3=name.split()
print(f"Инициалы: {n1[0].upper()}{n2[0].upper()}{n3[0].upper()}.")
print(f"Длина: {len(n1)+len(n2)+len(n3)}")