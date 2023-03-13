import os
from bitarray import bitarray

class Compression:
    def __init__(self, arbre):
        self.arbre = arbre
        self.tauxCompression = 0
        self.nbMoyenBit = 0

    def texte_binaire(self, fichier,liste_parcours_profondeur):
        """ Converti le texte d'origine en un texte binaire, grâce a un parcours en profondeur de l'arbre """

        txt_binaire = ''
        for lettre in fichier.lire_fichier(): # parcours des caractères du fichier txt
            for i in range(len(liste_parcours_profondeur)): # parcours de la liste obtenue grâce au parcours en profondeur de l'arbre
                if liste_parcours_profondeur[i][0] == f"'{lettre}'": # cherche dans liste_parcours_profondeur la lettre souhaité
                    txt_binaire += liste_parcours_profondeur[i][2] # le code de la lettre trouvée est ajouté à la chaine de caractère "txt_binaire"
        return txt_binaire

    def taux_compression(self, cheminFichier):
        """ Calcul du taux de compression par rapport au volume final et au volume initial """

        volume_final = os.path.getsize(f"{cheminFichier.split('.')[0]}/{cheminFichier.split('.')[0]}_comp.bin")
        volume_initial = os.path.getsize(cheminFichier)
        taux = 1 - volume_final/volume_initial
        self.tauxCompression = taux

    def nombre_moyen_bit(self,liste_parcours_profondeur):
        """ Calcul du nombre moyen de Bit du fichier compressé à partir du parcours en profondeur """

        nb_element = len(liste_parcours_profondeur) 
        bits_total = 0
        for i in range(nb_element):
            bits_total += len(liste_parcours_profondeur[i][2])
        self.nbMoyenBit= bits_total/nb_element    

    def fichier_texte_compresse(self, fichier, cheminFichier):
        """ Creation du fichier compressé """

        liste_parcours_profondeur = self.arbre.parcours_profondeur()
        bits = self.texte_binaire(fichier,liste_parcours_profondeur)
        bits = bits.strip() #supprime les espaces,tabulations et sauts de lignes
        liste_entiers = []

        for element in bits:
            liste_entiers.append(int(element))

        bits = bitarray(liste_entiers)
        
        #creation d'un dossier avec pour nom le nom du fichier si il n'existe pas déjà
        chemin_dossier = f"{cheminFichier.split('.')[0]}/"
        if not os.path.exists(chemin_dossier):
            os.makedirs(chemin_dossier)
            
        with open(f"{chemin_dossier}/{cheminFichier.split('.')[0]}_comp.bin", "wb") as nouv_fichier:
            bits.tofile(nouv_fichier)
        
        # Données obtenues à partir du fichier_texte_compresse
        self.taux_compression(cheminFichier) #ajout du taux de compression du fichier compressé
        self.nombre_moyen_bit(liste_parcours_profondeur) #ajout du nombre moyen de bits du fichier compressé