class Odam:
    def __init__(self, ismi, familiyasi, yoshi):
        self.ismi = ismi
        self.familiyasi = familiyasi
        self.yoshi = yoshi
    def __str__(self):
        return "Ismi: {}, Familiyasi: {}, Yoshi: {}".format(self.ismi, self.familiyasi, self.yoshi)
class Ishchi(Odam):
    def __init__(self, ismi, familiyasi, yoshi, turi):
        super().__init__(ismi, familiyasi, yoshi)
        self.turi = turi
    def __str__(self):
        text = super(Ishchi, self).__str__()
        text += ", Kasbi: {}".format(self.turi)
        return text
ishchi =  Ishchi("Rahim", "Quchqorov", 32, "O'qituvchi")
# print(ishchi)
class bemor(Odam):
    def __init__(self, ismi, familiyasi, yoshi, shikoyati):
        super().__init__(ismi, familiyasi, yoshi)
        self.shikoyati = shikoyati
    def __str__(self):
        text = super(bemor, self).__str__()
        text += ", Shikoyati {}".format(self.shikoyati)
        return text
Bemor = bemor("O'ral" , "Xolboyev", 30, "Tish og'rig'i")
# print(Bemor)
class talaba(Odam):
    def __init__(self, ismi, familiyasi, yoshi, kursi):
        super().__init__(ismi, familiyasi, yoshi)
        self.kursi = kursi
    def __str__(self):
        text = super(talaba, self).__str__()
        text += ", Kursi: {}".format(self.kursi)
        return text
Talaba = talaba("Kamron", "Alikhanov", 20, "2-kurs")
print(Talaba)