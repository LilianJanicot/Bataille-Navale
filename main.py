from gril.grille import Grille
from boat.bateau import PorteAvion, Torpilleur, Croiseur, Sousmarin
from random import randrange, choice

grilleFront=Grille(8,10)
grilleBack=Grille(8,10)

while True:
    l,c=randrange(0,8),randrange(0,10)
    vertical=choice([True,False])
    monPorteAvion=PorteAvion(l,c,vertical)
    ajout=grilleBack.ajoute(monPorteAvion)
    if ajout:
        break

while True:
    l,c=randrange(0,8),randrange(0,10)
    vertical=choice([True,False])
    monCroiseur=Croiseur(l,c,vertical)
    ajout=grilleBack.ajoute(monCroiseur)
    if ajout:
        break

while True:
    l,c=randrange(0,8),randrange(0,10)
    vertical=choice([True,False])
    monTorpilleur=Torpilleur(l,c,vertical)
    ajout=grilleBack.ajoute(monTorpilleur)
    if ajout:
        break

while True:
    l,c=randrange(0,8),randrange(0,10)
    vertical=choice([True,False])
    monSousmarin=Sousmarin(l,c,vertical)
    ajout=grilleBack.ajoute(monSousmarin)
    if ajout:
        break
listeSymbole=["🚢","⛴","🚣","🐟"]
while not(monSousmarin.coule(grilleFront) and monCroiseur.coule(grilleFront) and monTorpilleur.coule(grilleFront) and monPorteAvion.coule(grilleFront)):
    grilleFront.afficher()
    entree = input("Entrez les coordonées séparées par un espace : ")
    l, c = map(int, entree.split())
    indice=l*grilleBack.colonne+c
    if grilleBack.matrice[indice]=="🚢":
        grilleFront.tirer(l,c,"💣")    
        if monPorteAvion.coule(grilleFront):
            for x in monPorteAvion.positions:
                a,b=x
                grilleFront.tirer(a,b,"🚢")
            print("Touché coulé!")
        else:
            print("Touché!")
    elif grilleBack.matrice[indice]=="⛴":
        grilleFront.tirer(l,c,"💣")    
        if monCroiseur.coule(grilleFront):
            for x in monCroiseur.positions:
                a,b=x
                grilleFront.tirer(a,b,"⛴")
            print("Touché coulé!")
        else:
            print("Touché!")
    elif grilleBack.matrice[indice]=="🚣":
        grilleFront.tirer(l,c,"💣")    
        if monTorpilleur.coule(grilleFront):
            for x in monTorpilleur.positions:
                a,b=x
                grilleFront.tirer(a,b,"🚣")
            print("Touché coulé!")
        else:
            print("Touché!")
    elif grilleBack.matrice[indice]=="🐟":
        grilleFront.tirer(l,c,"💣")    
        if monSousmarin.coule(grilleFront):
            for x in monSousmarin.positions:
                a,b=x
                grilleFront.tirer(a,b,"🐟")
            print("Touché coulé!")
        else:
            print("Touché!")
    else:
        grilleFront.tirer(l,c)
        print("Raté")

grilleFront.afficher()
print("Tu as gagné!!")