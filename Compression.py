import os
import struct

class Compression:
    def __init__(self, arbre):
        self.arbre = arbre

    def texte_binaire(self, fichier_texte_origine):
        """ Retourne un texte binaire correspondant au texte d'origine """
        txt_binaire = ''
        liste_parcours_profondeur = self.arbre.parcours_profondeur()
        for lettre in fichier_texte_origine.lire_fichier():
            for i in range(len(liste_parcours_profondeur)):
                if liste_parcours_profondeur[i][0] == f"'{lettre}'":
                    txt_binaire += liste_parcours_profondeur[i][2]
        return txt_binaire

    def texte_binaire_conversion_octet(self, fichier_texte_origine):
        """ Converti le texteBinaire en Octets """
        bits = self.texte_binaire(fichier_texte_origine)
        bits = bits.strip()
        if len(bits) % 8 != 0:
            bits = bits.zfill(len(bits) + 8 - len(bits) % 8)
        return bytes([int(bits[i:i+8], 2) for i in range(0, len(bits), 8)])

    def fichier_texte_compresse(self, fichier, fichier_texte_origine):

        chemin_dossier = f"{fichier_texte_origine.split('.')[0]}/"
        if not os.path.exists(chemin_dossier):
            os.makedirs(chemin_dossier)

        bytes_data = self.texte_binaire_conversion_octet(fichier)
        with open(f"{chemin_dossier}/{fichier_texte_origine.split('.')[0]}_comp.bin", "wb") as nouv_fichier:
            packed_data = struct.pack("%dB" % len(bytes_data), *bytes_data)
            nouv_fichier.write(packed_data)

