import os

class MonFichier:
    
    def __init__(self, nom_fichier):
        self.nom_fichier = nom_fichier

    def lire_fichier(self):
        with open(self.nom_fichier, 'r') as fichier:
            return fichier.read()
        
    """ Creation d'un dictionnaire (non trié) avec les caratères et leur fréquence """
    def frequence(self):
        frequence = {}

        # Parcours du fichier texte lu
        for lettre in self.lire_fichier():

            # Verification de la presence ou non du caractere dans le dictionnaire frequence
            if lettre not in frequence.keys():
                frequence[lettre] = 1
            else:
                frequence[lettre] += 1

        return frequence

    """ Dictionnaire final trié: l'ordre des caractères de l’alphabet est maintenu par fréquence croissante puis par ordre de codage des caractères ASCII """
    def alphabet_trie(self):
        f = self.frequence()
        alphabet = dict(sorted(f.items(), key=lambda t: t[0])) # tri de l'alphabet par ordre croissant de cle (frequence)
        alphabet = dict(sorted(alphabet.items(), key=lambda t: t[1])) # tri de l'aplphabet par ordre croissant de valeur (caractere)
        return alphabet

    """ Creation d'un fichier avec les caratères et leur fréquence """
    def creation_fichier_alphabet(self):

        chemin_dossier = f"{self.nom_fichier.split('.')[0]}/"
        if not os.path.exists(chemin_dossier):
            os.makedirs(chemin_dossier)

        # creation du nouveau fichier avec comme nom: le nom du fichier sans l'extension ainsi que "_freq.txt"
        # ".split(.)" separe le texte à partir du point et [0] affiche seulement le premier element 
        with open(f"{chemin_dossier}/{self.nom_fichier.split('.')[0]}_freq.txt", "w") as nouv_fichier:

            # taille de l'alphabet
            nouv_fichier.write(f"{str(len(self.alphabet_trie()))} \n")

            # Ecriture des caractères et de leur fréquence dans le nouveau fichier
            for cle,valeur in self.alphabet_trie().items():
                nouv_fichier.write(f"{cle} {valeur} \n")

    