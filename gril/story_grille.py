from grille import Grille

maGrille=Grille(5,8)
while 1!=0:
    maGrille.afficher()
    entree = input("Entrez les coordonées séparées par un espace : ")
    x, y = map(int, entree.split())
    maGrille.tirer(x,y)
