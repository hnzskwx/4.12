class Student:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek
        self.predmety = []
        self.znamky = []
        self.prumer = None

    def pridej_predmet(self, predmet):
        self.predmety.append(predmet)

    def ziskej_prumer(self):
        if len(self.znamky) > 0:
            self.prumer = sum(self.znamky) / len(self.znamky)
            return self.prumer
        else:
            return "Žádné známky k výpočtu průměru."

    def pridej_znamku(self, znamka):
        self.znamky.append(znamka)

    def informace(self):
        info = f"Jméno: {self.jmeno}\nVěk: {self.vek}\nPředměty: {', '.join(self.predmety)}\n"
        if self.prumer is not None:
            info += f"Průměr: {self.prumer}"
        else:
            info += "Průměr: Neznámý"
        return info


class Teacher:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek
        self.predmety = []
        self.studenti = []

    def pridat_studenta(self, student):
        self.studenti.append(student)

    def odebrat_studenta(self, student):
        if student in self.studenti:
            self.studenti.remove(student)
            return f"Student {student.jmeno} odebrán."
        else:
            return "Student nenalezen v seznamu."

    def informace(self):
        info = f"Jméno učitele: {self.jmeno}\nVěk: {self.vek}\nPředměty: {', '.join(self.predmety)}\n"
        if len(self.studenti) > 0:
            info += "Seznam studentů:\n"
            for student in self.studenti:
                info += f"{student.jmeno}\n"
        else:
            info += "Žádní studenti v seznamu."
        return info



student1 = Student("Jan Novák", 18)
student1.pridej_predmet("Matematika")
student1.pridej_predmet("Fyzika")


student1.pridej_znamku(90)
student1.pridej_znamku(85)


ucitel1 = Teacher("Mgr. Karla Malá", 35)
ucitel1.pridat_studenta(student1)


print(student1.informace())
print("\n")
print(ucitel1.informace())
