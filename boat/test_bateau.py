from bateau import Bateau
def test_init():
    monBateau=Bateau(2,3)
    assert monBateau.ligne==2
    assert monBateau.colonne==3
    assert monBateau.longueur==1
    assert monBateau.vertical==False
    monBateau=Bateau(4,8,5,True)
    assert monBateau.ligne==4
    assert monBateau.colonne==8
    assert monBateau.longueur==5
    assert monBateau.vertical==True

def test_positions():
    assert Bateau(2, 3, longueur=3).positions==[(2, 3), (2, 4), (2, 5)]
    assert Bateau(2, 3, longueur=3, vertical=True).positions == [(2, 3), (3, 3), (4, 3)]

def test_coule():
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parent.parent))
    from gril.grille import Grille
    monBateau=Bateau(0,0,3)
    maGrille=Grille(3,3)
    assert monBateau.coule(maGrille)==False
    maGrille.tirer(0,0)
    maGrille.tirer(0,1)
    maGrille.tirer(0,2)
    assert monBateau.coule(maGrille)==True

def test_porteavion():
    from bateau import PorteAvion
    monPorteAvion=PorteAvion(1,2)
    assert type(monPorteAvion) is PorteAvion
    assert monPorteAvion.longueur == 4

def test_croiseur():
    from bateau import Croiseur
    monCroiseur=Croiseur(1,2)
    assert type(monCroiseur) is Croiseur
    assert monCroiseur.longueur == 3

def test_torpilleur():
    from bateau import Torpilleur
    monTorpilleur=Torpilleur(1,2)
    assert type(monTorpilleur) is Torpilleur
    assert monTorpilleur.longueur == 2

def test_sousmarin():
    from bateau import Sousmarin
    monSousmarin=Sousmarin(1,2)
    assert type(monSousmarin) is Sousmarin
    assert monSousmarin.longueur == 2