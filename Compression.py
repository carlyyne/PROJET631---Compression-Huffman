import os
import struct
from bitarray import bitarray

class Compression:
    def __init__(self, arbre):
        self.arbre = arbre

    def texte_binaire(self, fichier):
        """ Retourne un texte binaire correspondant au texte d'origine """
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

