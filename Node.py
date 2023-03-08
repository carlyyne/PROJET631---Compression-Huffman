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
