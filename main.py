# envoie Git
# git add .
# git commit -m "message"
# git push
# git status (à jour)

from MonFichier import MonFichier
from Compression import Compression
from ArbreHuffman import ArbreHuffman

if __name__ == "__main__":

    ############################### FICHIERS À DISPOSITION ###############################
    fichierTexte = 'extraitalice.txt'
    fichierTexte1 = 'alice.txt'
    fichierTexte2 = "textesimple.txt"
    fichier = fichierTexte2

    f = MonFichier(fichier) # à changer suivant le texte

    ########## ETAPE 1: DETERMINATION DE L'ALPHABET ET FREQUENCES DES CARACTERES ##########
    Alphabet = f.alphabet_trie()
    f.creation_fichier_alphabet()

    ########################## ETAPE 2: CONSTRUCTION DE L'ARBRE ##########################
    arbre = ArbreHuffman(f)
    arbre.construction_arbre_codage(Alphabet)
    arbre.afficher_arbre_binaire().render(f"{fichier.split('.')[0]}/tree") # à changer suivant le texte

    ############################## ETAPE 3: CODAGE DU TEXTE ##############################
    c = Compression(arbre)
    c.fichier_texte_compresse(f,fichier) # à changer suivant le texte
    
    ################### ETAPE 4: DETERMINATION DU TAUX DE COMPRESSION ###################
    print("Taux de compression: "+ str(c.tauxCompression)) #a changer suivant le texte

    ################### ETAPE 5 : DÉTERMINATION NOMBRE MOYEN DE BITS ################### 
    print("Nombre moyen de bits de stockage d’un caractère du texte compressé: " + str(c.nbMoyenBit))  

    