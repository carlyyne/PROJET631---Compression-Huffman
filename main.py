from MonFichier import MonFichier
from Compresseur import Compresseur
from ArbreHuffman import ArbreHuffman

def run(cheminFichierTxt):

    f = MonFichier(cheminFichierTxt)

    ########## ETAPE 1: DETERMINATION DE L'ALPHABET ET FREQUENCES DES CARACTERES ##########
    Alphabet = f.alphabet_trie()
    f.creation_fichier_alphabet()

    ########################## ETAPE 2: CONSTRUCTION DE L'ARBRE ##########################
    arbre = ArbreHuffman(f)
    arbre.construction_arbre_codage(Alphabet)
    arbre.afficher_arbre_binaire().render(f"{f.nom_fichier.split('.')[0]}/tree")

    ############################## ETAPE 3: CODAGE DU TEXTE ##############################
    fc = Compresseur(arbre)
    fc.fichier_texte_compresse(f,f.nom_fichier)
    
    ################### ETAPE 4: DETERMINATION DU TAUX DE COMPRESSION ###################
    print("----------- "+cheminFichierTxt + " -----------")
    print("Taux de compression: " + str(fc.tauxCompression))

    ################### ETAPE 5 : DÉTERMINATION NOMBRE MOYEN DE BITS ################### 
    print("Nombre moyen de bits de stockage d’un caractère: " + str(fc.nbMoyenBit))  

if __name__ == "__main__":

    ############################### FICHIERS À DISPOSITION ###############################
    fichierTexte = "textesimple.txt"
    fichierTexte1 = "extraitalice.txt"
    fichierTexte2 = "alice.txt"

    ############################## COMPRESSION DES FICHIERS ##############################
    run(fichierTexte)
    run(fichierTexte1)
    run(fichierTexte2)


    