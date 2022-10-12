city = {"Uzbekistan":'Tashkent',
        'Russian':'Moscow',
        'USA':'Nyu-york',
        'Kazakhstan':'Astana',
        'Kyrgizistan':'O\'sh',
        'Australia':'Kuala-Lumpur',
        'Great Britain':'London'}
poytaxt = input('Davlat nomini kiriting:\n>>>')
if poytaxt in city:
    print(f"{poytaxt}ning poytaxti {city[poytaxt]} shaxri")
else:
    print("Bizda bunday ma'lumot yo'q")