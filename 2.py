class Odam:
    def __init__(self, ismi, familiyasi, yoshi):
        self.ismi = ismi
        self.familiyasi = familiyasi
        self.yoshi = yoshi
    def __str__(self):
        return "Ismi: {}, Familiyasi: {}, Yoshi: {}".format(self.ismi, self.familiyasi, self.yoshi)
odam1 = Odam("Akmal", "Aliqulov", 22)
print(odam1)