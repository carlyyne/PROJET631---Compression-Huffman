import os
from bitarray import bitarray

class Compression:
    def __init__(self, arbre):
        self.arbre = arbre
        self.tauxCompression = 0
        self.nbMoyenBit = 0

    def texte_binaire(self, fichier):
        """ Retourne un texte binaire correspondant au texte d'origine grâce a un parcours en profondeur de l'arbre"""
        txt_binaire = ''
        liste_parcours_profondeur = self.arbre.parcours_profondeur()
        for lettre in fichier.lire_fichier():
            for i in range(len(liste_parcours_profondeur)):
                if liste_parcours_profondeur[i][0] == f"'{lettre}'":
                    txt_binaire += liste_parcours_profondeur[i][2]
        return txt_binaire

    
    def fichier_texte_compresse(self, fichier, fichier_texte_origine):
        
        """ Converti le texteBinaire en Octets """
        bits = self.texte_binaire(fichier)
        bits = bits.strip() #supprime les espaces,tabulations et sauts de lignes
        liste_bits = []

        for element in bits:
            liste_bits.append(int(element))

        octets = bitarray(liste_bits)
        
        #creation d'un dossier avec pour nom le nom du fichier si il n'existe pas déjà
        chemin_dossier = f"{fichier_texte_origine.split('.')[0]}/"
        if not os.path.exists(chemin_dossier):
            os.makedirs(chemin_dossier)
            
        with open(f"{chemin_dossier}/{fichier_texte_origine.split('.')[0]}_comp.bin", "wb") as nouv_fichier:
            octets.tofile(nouv_fichier)
        
        liste_parcours_profondeur = self.arbre.parcours_profondeur()
        self.taux_compression(fichier_texte_origine) #ajout du taux de compression du fichier compressé
        self.nombre_moyen_bit(liste_parcours_profondeur) #ajout du taux de compression du fichier compressé

    """ Calcul du taux de compression par rapport au volume final et au volume initial """
    def taux_compression(self, nomFichier):
        volume_final = os.path.getsize(f"{nomFichier.split('.')[0]}/{nomFichier.split('.')[0]}_comp.bin")
        volume_initial = os.path.getsize(nomFichier)
        taux = 1 - volume_final/volume_initial
        self.tauxCompression = taux


    """ Calcul du nombre moyen de Bit du fichier compressé à partir du parcours en profondeur """
    def nombre_moyen_bit(self,liste_parcours_profondeur):
        nb_element = len(liste_parcours_profondeur) 
        bits_total = 0
        for i in range(nb_element):
            bits_total += len(liste_parcours_profondeur[i][2])
        self.nbMoyenBit= bits_total/nb_element    