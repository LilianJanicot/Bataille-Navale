from grille import Grille

def test_init():
    maGrille=Grille(3,7)
    assert len(maGrille.matrice)==3*7
    assert maGrille.colonne==7

def test_tirer():
    maGrille=Grille(3,7)
    assert maGrille.matrice[2*maGrille.colonne+4]=="~"
    maGrille.tirer(2,4)
    assert maGrille.matrice[2*maGrille.colonne+4]=="x"
    assert maGrille.matrice[1*maGrille.colonne]=="~"

def test_afficher():
    maGrille=Grille(2,3)
    assert str(maGrille)=="~~~\n~~~\n"

def test_ajoute():
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parent.parent))
    from boat.bateau import Bateau
    maGrille=Grille(2,4)
    monBateau1=Bateau(0,1,2,True)
    maGrille.ajoute(monBateau1)
    assert str(maGrille)=="~⛵~~\n~⛵~~\n"
    monBateau2=Bateau(0,1,2)
    maGrille.ajoute(monBateau2)
    assert str(maGrille)=="~⛵~~\n~⛵~~\n"