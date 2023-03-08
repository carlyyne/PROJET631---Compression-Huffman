import graphviz

class Node:
    def __init__(self, char, freq, leftChild = None, rightChild = None,code = ""):
        self.char = char
        self.freq = freq
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.code = code

    # surcharge operateur < pour la fonction 'sort()'
    def __lt__(self, other):
        return self.freq < other.freq
    
    def parcoursProfondeur(self):
        res = []
        nb = f"0{str(len(self.code))}b"
        if self.code != '':
            res.append([self.char, self.freq, format(int(self.code,2),nb)])
        else:
            res.append([self.char, self.freq, self.code])
            
        if self.leftChild:
            self.leftChild.code = self.code + "0"
            res += self.leftChild.parcoursProfondeur()
        if self.rightChild:
            self.rightChild.code = self.code + "1"
            res += self.rightChild.parcoursProfondeur()
        return res


def ConstructionArbreCodage(alphabet):
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

def afficher_arbre_binaire(root):

    # id(): retourne un identifiant unique pour chaque objet, ce qui garantit que chaque nœud de l'arbre aura un identifiant distinct dans l'objet Graphviz.
    graph = graphviz.Digraph()
    graph.node(str(id(root)), label=str(root.freq))

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

    ajouter_noeud(root)
    return graph