price=float(input("PRICE:"))
discount=float(input("DISCOUNT:"))
vat=float(input("VAT:"))
base=price*(1-discount/100)
vat_amount=base*vat/100
total=base+vat_amount
print(f"БАЗА ПОСЛЕ СКИДКИ: {base:.2f}")
print(f"СУММА НДС: {vat_amount:.2f}")
print(f"ОБЩАЯ СУММА: {total:.2f}")