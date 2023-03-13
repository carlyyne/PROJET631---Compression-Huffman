
import graphviz
from Node import Node

class ArbreHuffman:
    
    def __init__(self,file):
        self.file = file
        self.racine = self.construction_arbre_codage(file.alphabet_trie())
    
    def construction_arbre_codage(self,alphabet):
        """ Construction du l'arbre d'Huffman """
        listeNoeuds =[]

        #creation liste de noeuds pour chaque caractere de l'alphabet avec la frequence associée
        for char, freq in alphabet.items():
            listeNoeuds.append(Node(f"'{char}'",freq))
    
        while len(listeNoeuds) > 1: #Jusqu'à ce qu'il reste plus qu'un seul arbre
            t1 = listeNoeuds[0]
            t2 = listeNoeuds[1]
            listeNoeuds = listeNoeuds[2:] #modifie la liste pour enlever les 2 premiers noeuds ayant les plus basses frequences: t1 et t2
            t = Node("",t1.freq+t2.freq,t1,t2) #creation d'un nouvel arbre t
            listeNoeuds.append(t)
            listeNoeuds.sort() #tri de listeNoeuds par frequence

        return listeNoeuds[0] # l'arbre restant

    def parcours_profondeur(self):
        return self.racine.parcours_profondeur()
    
    def afficher_arbre_binaire(self):
        """ affiche l'arbre binaire dans un .pdf pour avoir un aperçu grâce au module de visualisation graphviz """

        graph = graphviz.Digraph() # Création d'un objet Graphviz
        self.ajouter_noeud(graph,self.racine) # Ajout de la racine de l'arbre
        return graph # Retourne l'objet Graphviz représentant l'arbre binaire
    
    def ajouter_noeud(self, graph, noeud):
        
        # ajout du noeud à graphviz avec son nom et sa fréquence
        # id(): retourne un identifiant unique pour chaque objet, ce qui garantit que chaque nœud de l'arbre aura un identifiant distinct dans l'objet Graphviz.
        graph.node(str(id(noeud)), label=f"{noeud.char}({noeud.freq})") 

        if noeud.leftChild:
            # ajout du fils gauche
            self.ajouter_noeud(graph, noeud.leftChild)
            # ajout de l'arc reliant le noeud courant à son fils gauche
            graph.edge(str(id(noeud)), str(id(noeud.leftChild)), label="0")

        if noeud.rightChild:
            # ajout du fils droit
            self.ajouter_noeud(graph, noeud.rightChild)
            # ajout de l'arc reliant le noeud courant à son fils droit
            graph.edge(str(id(noeud)), str(id(noeud.rightChild)), label="1") 