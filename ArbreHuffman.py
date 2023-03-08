import graphviz
from Node import Node

class ArbreHuffman:
    
    def __init__(self,file):
        self.file = file
        self.racine = self.ConstructionArbreCodage(file.alphabet_trie())
    
    def ConstructionArbreCodage(self,alphabet):
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
        return self.racine.parcoursProfondeur()
        
    def afficher_arbre_binaire(self):

        # id(): retourne un identifiant unique pour chaque objet, ce qui garantit que chaque nœud de l'arbre aura un identifiant distinct dans l'objet Graphviz.
        graph = graphviz.Digraph()
        graph.node(str(id(self.racine)), label=str(self.racine.freq))

        def ajouter_noeud(node):
            if node.leftChild:
                if node.leftChild.char != "":
                    graph.node(str(id(node.leftChild)), label=f"{str(node.leftChild.freq)},{node.leftChild.char}") 
                else:
                    graph.node(str(id(node.leftChild)), label=str(node.leftChild.freq))
                graph.edge(str(id(node)), str(id(node.leftChild)),'0')
                ajouter_noeud(node.leftChild)
            if node.rightChild:
                if node.rightChild.char != "":
                    graph.node(str(id(node.rightChild)), label=f"{str(node.rightChild.freq)},{node.rightChild.char}")
                else:
                    graph.node(str(id(node.rightChild)), label=str(node.rightChild.freq))
                graph.edge(str(id(node)), str(id(node.rightChild)),'1')
                ajouter_noeud(node.rightChild)

        ajouter_noeud(self.racine)
        return graph