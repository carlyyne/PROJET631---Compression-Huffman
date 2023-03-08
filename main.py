# envoie Git
# git add .
# git commit -m "message"
# git push
# git status (à jour)

from MonFichier import MonFichier
from Compression import Compression
from ArbreHuffman import ArbreHuffman

# Calcul du taux de compression par rapport au volume final et au volume initial
def taux_compression(fichier_texte_compresse, texte_lu_origine):
    volume_final = len(fichier_texte_compresse)
    volume_initial = len(texte_lu_origine)
    taux = 1 - volume_final/volume_initial
    return taux

#Calcul du nombre moyen de Bit du fichier compressé à partir du parcours en profondeur
def nombre_moyen_bit(liste_parcours_prof):
    nb_element = len(liste_parcours_prof) 
    bits_total = 0
    for i in range(nb_element):
        bits_total += len(liste_parcours_prof[i][2])
    return bits_total/nb_element

if __name__ == "__main__":

    ############################### FICHIERS À DISPOSITION ###############################
    fichierTexte = 'extraitalice.txt'
    fichierTexte1 = 'alice.txt'
    fichierTexte2 = "textesimple.txt"

    f = MonFichier(fichierTexte1) # à changer suivant le texte

    ########## ETAPE 1: DETERMINATION DE L'ALPHABET ET FREQUENCES DES CARACTERES ##########
    Alphabet = f.alphabet_trie()
    f.creation_fichier_alphabet()

    ########################## ETAPE 2: CONSTRUCTION DE L'ARBRE ##########################
    arbre = ArbreHuffman(f)
    arbre.ConstructionArbreCodage(Alphabet)
    arbre.afficher_arbre_binaire().render(f"{fichierTexte1.split('.')[0]}/tree") # à changer suivant le texte

    ############################## ETAPE 3: CODAGE DU TEXTE ##############################
    c = Compression(arbre)
    texteOctet = c.texte_binaire_conversion_octet(f)
    c.fichier_texte_compresse(f,fichierTexte1) # à changer suivant le texte
    
    ################### ETAPE 4: DETERMINATION DU TAUX DE COMPRESSION ###################
    print("Taux de compression: "+ str(taux_compression(texteOctet,f.lire_fichier())))

    ################### ETAPE 5 : DÉTERMINATION NOMBRE MOYEN DE BITS ################### 
    print("Nombre moyen de bits de stockage d’un caractère du texte compressé: " + str(nombre_moyen_bit(arbre.parcours_profondeur())))  

    