class Bateau:
    def __init__(self,ligne, colonne,longueur=1,vertical=False):
        self.ligne=ligne
        self.colonne=colonne
        self.longueur=longueur
        self.vertical=vertical
    
    @property
    def positions(self):
        liste=[]
        for i in range(self.longueur):
            if self.vertical:
                liste.append((self.ligne+i,self.colonne))
            else:
                liste.append((self.ligne,self.colonne+i))
        return liste
    
    def coule(self,grille):
        for x in self.positions:
            l,c=x
            if grille.matrice[l*grille.colonne+c] == "~":
                return False
        return True
