class Bateau:
    def __init__(self,ligne, colonne,longueur=1,vertical=False):
        self.ligne=ligne
        self.colonne=colonne
        self.longueur=longueur
        self.vertical=vertical
        self.hit="⛵"
    
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

class PorteAvion(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 4, vertical)
        self.hit="🚢"

class Croiseur(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 3, vertical)
        self.hit="⛴"

class Torpilleur(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 2, vertical)
        self.hit="🚣"

class Sousmarin(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, 2, vertical)
        self.hit="🐟"