import Node as N
import struct

# Détermination de l’alphabet et des frequences absolues de chaque caractere
def frequence(fichier):
    frequence = {}

    # Parcours du fichier texte lu
    for lettre in fichier:

        # Verification de la presence ou non du caractere dans le dictionnaire frequence
        if lettre not in frequence.keys():
            frequence[lettre] = 1
        else:
            frequence[lettre] += 1
            
    return frequence

def alphabet(fichier):
    f = frequence(fichier)
    alphabet = dict(sorted(f.items(), key=lambda t: t[0])) # tri de l'alphabet par ordre croissant de cle 
    alphabet = dict(sorted(alphabet.items(), key=lambda t: t[1])) # tri de l'aplphabet par ordre croissant de valeur
    return alphabet

def fichier_alphabet(fichiertexte,fichierLu):
    # fichier de description de l’alphabet utilisé avec les fréquences de caractère et sa taille
    nouvFichier = open(f"{fichiertexte.split('.')[0]}_freq.txt", "w") #nouveau fichier avec comme nom: le nom du fichier sans l'extension. 
                                                               # ".split(.)" separe le texte à partir du point et [0] affiche seulement le premier element 
    #taille de l'alphabet
    nouvFichier.write(f"{str(len(alphabet(fichierLu)))} \n")

    for cle,valeur in alphabet(fichierLu).items():
        nouvFichier.write(f"{cle} {valeur} \n")
    nouvFichier.close()

def TexteBinaire(fichierLu,arbre):
    """ Retourne un texte binaire correspondant au texte d'origine """
    txtBinaire=''
    listeParcoursProfondeur = arbre.parcoursProfondeur()
    for lettre in fichierLu:
            for i in range (len(listeParcoursProfondeur)):
                if listeParcoursProfondeur[i][0]==f"'{lettre}'":
                     txtBinaire += listeParcoursProfondeur[i][2]
    return txtBinaire

def TexteBinaire_ConversionOctet(bits):
    """ Converti le texteBinaire en Octets """
    bits = bits.strip()
    if len(bits) % 8 != 0:
        bits = bits.zfill(len(bits) + 8 - len(bits) % 8)
    return bytes([int(bits[i:i+8], 2) for i in range(0, len(bits), 8)])

def FichierTexteCompresse(fichierTexteOrigine, texteBinaire):
    bytes = TexteBinaire_ConversionOctet(texteBinaire)
    with open(f"{fichierTexteOrigine.split('.')[0]}_comp.bin", "wb") as nouvFichier:
        packed_data = struct.pack("%dB" % len(bytes), *bytes)
        nouvFichier.write(packed_data)

# Calcul du taux de compression par rapport au volume final et au volume initial
def tauxCompression(fichierTexteCompresse, texteLuOrigine):
    volumefinal = len(fichierTexteCompresse)
    volumeinitial = len(texteLuOrigine)
    taux = 1 - volumefinal/volumeinitial
    return taux

# Calcul du nombre moyen de Bit du fichier compressé à partir du parcours en profondeur
def NombreMoyenBit(listeParcousProf):
    nbElement = len(listeParcousProf) 
    bitsTotal = 0
    for i in range (nbElement):
        bitsTotal += len(listeParcousProf[i][2])
    return bitsTotal/nbElement

if __name__ == "__main__":

    ############################### FICHIERS À DISPOSITION ###############################
    fichierTexte = '/Users/carlynebarrachin/Documents/Polytech/FI3/S6/PROJ631-ALGO/Compression/extraitalice.txt'
    fichierTexte1 = '/Users/carlynebarrachin/Documents/Polytech/FI3/S6/PROJ631-ALGO/Compression/alice.txt'
    fichierTexte2 = '/Users/carlynebarrachin/Documents/Polytech/FI3/S6/PROJ631-ALGO/Compression/textesimple.txt'

    ############################## LECTURE D'UN DES FICHIERS ##############################
    f = open(fichierTexte2, 'r') # à changer suivant le texte
    fRead = f.read()

    ########## ETAPE 1: DETERMINATION DE L'ALPHABET ET FREQUENCES DES CARACTERES ##########
    Alphabet = alphabet(fRead)
    fichier_alphabet(fichierTexte2,fRead) # à changer suivant le texte

    ########################## ETAPE 2: CONSTRUCTION DE L'ARBRE ##########################
    arbre = N.ConstructionArbreCodage(Alphabet)
    N.afficher_arbre_binaire(arbre).render('Compression/output/tree')

    ############################## ETAPE 3: CODAGE DU TEXTE ##############################
    txtBinaire = TexteBinaire(fRead,arbre)
    FichierTexteCompresse(fichierTexte2, txtBinaire) # à changer suivant le texte
    
    ################### ETAPE 4: DETERMINATION DU TAUX DE COMPRESSION ###################
    print("Taux de compression: "+ str(tauxCompression(TexteBinaire_ConversionOctet(txtBinaire),fRead)))

    ################### ETAPE 5 : DÉTERMINATION NOMBRE MOYEN DE BITS ################### 
    print("Nombre moyen de bits de stockage d’un caractère du texte compressé: " + str(NombreMoyenBit(arbre.parcoursProfondeur())))

    f.close()
    

    