# Bataille-Navale
Le jeu de la bataille navale à un joueur

<u>**Préparation :**</u> pour exécuter le jeu, il faut lancer le fichier main.py

<u>**But :**</u> des bateaux sont cachés sur la carte : un bateau de 4 cases de longueur, un de 3 et deux de 2. Votre but est de couler tous les bateaux en moins de coup possible.

<u>**Règles :**</u> à chaque tour, vous pouvez rentrer les coordonnées de où vous voulez tirer sur la grille.
S'il y a un bateau, une 💣 s'affichera avec le message "Touché" en haut et vous rejouez.
Si vous coulez le bateau, il s'affichera sur la carte avec l'un des symboles suivants:🚢,⛴,🚣,🐟 avec le texte "Touché coulé!" et vous rejouez
S'il n'y a pas de bateau, le symbole x s'affichera avec le message "Raté". Vous utilisez un nouveau tir pour continuer.

<u>**Fin de partie :**</u> le jeu se termine quand il n'y a plus de bateaux sur la carte. Votre score est affiché avec le message de victoire.

<u>**Spécificité :**</u> 
A chaque tour, le programme vous demandera de rentrer votre coup. Il faut le rentrer ainsi : **ligne ESPACE colonne**
Exemple :   3 5 (fonctionne)
            4,5 (ne fonctionne pas)
            7 8 (fonctionne)

Il faut que **ligne et colonne soient comprises dans la grille** sinon votre partie s'arrête.
A savoir que **l'indexation commence à 0.** Ainsi, ligne accepte les valeurs suivantes pour un tableau de 8 ligne : 0,1,2,3,4,5,6,7 
