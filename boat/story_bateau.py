from bateau import Bateau

def cheuvauvement(bat1,bat2):
    chevauchement=False
    for x in bat1.positions :
        if x in bat2.positions :
            chevauchement=True
    if chevauchement:
        print("Il y a cheuvauchement")
    else:
        print("Il n'y a pas cheuvauchement")

b1=Bateau(2,4,5,True)
b2=Bateau(5,4,8, False)

cheuvauvement(b1,b2)

b1=Bateau(2,4,5,True)
b2=Bateau(7,4,8, False)

cheuvauvement(b1,b2)