python_dict = {'float':'butun sonlar',
               'def':'funksiya',
               'integer':'natural sonlar',
               'value':'qiymat',
               'print':'chop etmoq',
               'error':'xato',
               'string':'matn',
               'for':'uchun',
               'if':'agar',
               'type':"ma'lumot turi"
               }
surov = input("Biror operatorni kiriting:\n>>>")
if surov in python_dict:
    print(f"{surov} atamasi {python_dict[surov]} deb tarjima qilinadi.")
else:
    print("Lug'atda bunday operator yo'q ekan.")
