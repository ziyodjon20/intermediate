taomlar = {'Osh':38000,
           'Free':15000,
           'Somsa':7000,
           'Lagmon':20000,
           'Lavash':22000,
           'Shurva':18000,
           }
print("3 ta taom kiriting:")
taom1 = input("Birinchisiga nima buyurasiz?\n>>>")
if taom1.title() in taomlar:
    print(f"{taom1}:{taomlar[taom1.title()]}")
taom2 = input("Ikkinchisiga nima buyurasiz?\n>>>")
if taom2.title() in taomlar:
    print(f"{taom2}:{taomlar[taom2.title()]}")
taom3 = input("Uchinchisiga nima buyurasiz?\n>>>")
if taom3.title() in taomlar:
    print(f"{taom3}:{taomlar[taom3.title()]}")
else:print("Bizda bunday ovqat yo'q uzr!")

print(f"Umumiy hisobingiz {taomlar[taom1.title()]+taomlar[taom2.title()]+taomlar[taom3.title()]} so'm bo'ldi! Tashakkur!!!")