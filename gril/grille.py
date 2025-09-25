class Grille:
    vide = "~"
    def __init__(self,ligne,colonne):
        self.colonne = colonne
        self.matrice = ["~" for i in range(ligne * colonne)]
    def tirer(self,l,c):
        self.matrice[l*self.colonne+c]="x"
    def __str__(self):
        monString=""
        for l in range(len(self.matrice)//self.colonne):
            for c in range(self.colonne):
                monString+=self.matrice[l*self.colonne+c]
            monString+="\n"
        return monString
    def afficher(self):
        print(self)