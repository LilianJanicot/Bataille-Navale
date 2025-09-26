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
    def ajoute(self,bateau):
        #vérification que je peux mettre un bateau
        ajoutable=True
        i=0
        maListe=[]
        while i!=len(self.matrice)//self.colonne:
            for j in range(self.colonne):
                maListe.append((i,j))
            i+=1
        for x in bateau.positions:
            if x not in maListe:
                ajoutable=False
        if ajoutable:
        #ajouter le bateau
            for x in bateau.positions:
                l,c=x
                self.matrice[l*self.colonne+c]="⛵"
        