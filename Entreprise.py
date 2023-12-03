class employe:
    count1 = 0

    def __init__(self, nom, numDemploye, salaireBase):
        self._nom = nom
        self._numDemploye = numDemploye
        self._salaireBase = salaireBase
        employe.count1 += 1

    @property
    def get_nom(self):
        return self._nom

    @property
    def get_numDemploye(self):
        return self._numDemploye

    def calculer_salaire(self):
        return self._salaireBase

    def promouvoir(self, other):
        if other.heure_travaille >= 70:
            other = directeur(other._nom, other._numDemploye, other._salaireBase + other.heure_travaille * other.taux_horaire, other.prim_direction)
            return f"L'employe {self._nom} est devenu un directeur"
        if isinstance(other, employe_regulier) and other.heure_travaille >= 15:
            other = manager(other._nom, other._numDemploye, other._salaireBase + other.heure_travaille * other.taux_horaire, other.prim_gestion)
            return f"L'employe {self._nom} est devenu un manager"
        else:
            return "Nombre d'heure est insuffisant"


class manager(employe):
    count2 = 0

    def __init__(self, nom, numDemploye, salaireBase, prim_gestion):
        super().__init__(nom, numDemploye, salaireBase)
        self.prim_gestion = prim_gestion
        manager.count2 += 1

    def calculer_salaire(self):
        return self._salaireBase + self.prim_gestion


class directeur(employe):
    count3 = 0

    def __init__(self, nom, numDemploye, salaireBase, prim_direction):
        super().__init__(nom, numDemploye, salaireBase)
        self.prim_direction = prim_direction
        directeur.count3 += 1

    def calculer_salaire(self):
        return self._salaireBase + self.prim_direction


class employe_regulier(employe):
    count4 = 0

    def __init__(self, nom, numDemploye, salaireBase, heure_travaille):
        super().__init__(nom, numDemploye, salaireBase)
        self.heure_travaille = heure_travaille
        self.taux_horaire = 250
        self.prim_gestion = 0
        self.prim_direction = 0
        employe_regulier.count4 += 1

    def calculer_salaire(self):
        return self._salaireBase + (self.heure_travaille * self.taux_horaire)


# Example of usage
print("---------------Entreprise lharara---------------")
emp1 = employe("Salim Redaoui", 15, 3200)
emp2 = employe("Amina Clay", 23, 2500)
print("Salaire d'employe", emp1.get_nom, "est:", emp1.calculer_salaire(), "Dh")
print("Salaire d'employe", emp2.get_nom, "est:", emp2.calculer_salaire(), "Dh")
print("Nombre d'employe dans l'entreprise est:", employe.count1)
print("------------------------------------------------------------")
print("------------------------------------------------------------")
man1 = manager("Islam Slimani", 44, 9000, 700)
print("Le salaire du Manager", man1.get_nom, "est :", man1.calculer_salaire(), "Dh")
print("Nombre du manager dans l'entreprise est :", manager.count2)
print("------------------------------------------------------------")
print("------------------------------------------------------------")
dir1 = directeur("Hamid Zniber", 12, 20000, 3000)
dir2 = directeur("Nawal Etazi", 2, 17000, 2300)
dir3 = directeur("Khalid Aghbalo", 29, 22000, 3200)
print("Le salaire du directeur", dir1.get_nom, "est:", dir1.calculer_salaire(), "Dh")
print("Le salaire du directrice", dir2.get_nom, "est:", dir2.calculer_salaire(), "Dh")
print("Le salaire du directeur", dir3.get_nom, "est:", dir3.calculer_salaire(), "Dh")
print("Nombre de directeur dans l'entreprise est", directeur.count3)
print("------------------------------------------------------------")
print("------------------------------------------------------------")
empr1 = employe_regulier("Salah Dahbi", 90, 1000, 15)
empr2 = employe_regulier("Ayman Chwaker", 102, 1200, 75)
empr3 = employe_regulier("Salima Lherhori", 75, 1100, 10)
empr4 = employe_regulier("Iman Kechta", 56, 1000, 7)
print("Le salaire d'employe regulier", empr1.get_nom, "est:", empr1.calculer_salaire(), "Dh")
print(empr1.promouvoir(empr1),"\n")
print("Le salaire d'employe regulier", empr2.get_nom, "est:", empr2.calculer_salaire(), "Dh")
print(empr2.promouvoir(empr2),"\n")
print("Le salaire d'employe regulier", empr3.get_nom, "est:", empr3.calculer_salaire(), "Dh")
print(empr3.promouvoir(empr3),"\n")
print("Le salaire d'employe regulier", empr4.get_nom, "est:", empr4.calculer_salaire(), "Dh")
print(empr4.promouvoir(empr4),"\n")
print("Nombre d'employe regulier est", employe_regulier.count4)
