from ball import Ball
from vector import Vector3
import random
class ArbreBinaire:
    def __init__(self, nom, numero, gauche=None, droite=None):
        self.nom = nom
        self.numero = numero
        self.gauche = gauche
        self.droite = droite

def inserer_abr(nom, numero, abr):
    if abr is None:
        return ArbreBinaire(nom, numero, None, None)
    if nom == abr.nom:
        return abr
    if nom < abr.nom:
        abr.gauche = inserer_abr(nom, numero, abr.gauche)
    else:
        abr.droite = inserer_abr(nom,numero, abr.droite)
    return abr

def calculer_hauteur(noeud):
    """ Calcule la hauteur de l'arbre binaire. """
    if noeud is None:
        return -1  
    else:
        hauteur_gauche = calculer_hauteur(noeud.gauche)
        hauteur_droite = calculer_hauteur(noeud.droite)
        
        return max(hauteur_gauche, hauteur_droite) + 1

def write_tree_to_file(node, file, depth=0):
    if node is not None:
        # Use indentation based on depth
        file.write(' ' * depth + str(node.nom) + ' ' + str(node.numero) + '\n')
        print(' ' * depth + str(node.nom) + ' ' + str(node.numero))
        # Write left and right children with increased depth
        write_tree_to_file(node.gauche, file, depth + 1)
        write_tree_to_file(node.droite, file, depth + 1)


def read_tree_from_file(file):
    stack = []
    root = None
    
    for line in file:
        # Split the line into name and value
        parts = line.strip().split()
        if len(parts) != 2:
            continue  # Skip any malformed lines
        
        # Extract node name and value
        name, value = parts[0], int(parts[1])
        node = ArbreBinaire(name, value)

        # Calculate the depth based on leading spaces
        depth = len(line) - len(line.lstrip())
        
        if root is None:
            # Set the root node and add to stack
            root = node
            stack.append((node, depth))
        else:
            # Adjust stack to correct depth
            while stack and stack[-1][1] >= depth:
                stack.pop()
            
            # Check if we are adding a left or right child
            if stack:
                parent_node = stack[-1][0]
                if parent_node.gauche is None:
                    parent_node.gauche = node
                else:
                    parent_node.droite = node
            
            # Add the current node and its depth to the stack
            stack.append((node, depth))
    
    return root



def parcours_infixe_decroissant(abr, tab=[]):
    if abr is not None:
        parcours_infixe_decroissant(abr.droite, tab)
        tab.append(Ball((random.randint(0, 500), random.randint(0, 500), 0), vector=(Vector3((random.random(), random.random(), 0))), nom=abr.nom, num=abr.numero, radius=10))
        parcours_infixe_decroissant(abr.gauche, tab)

    return tab

def loadtree():
    with open('tree.txt', 'r') as file:
        arbre_nom_num = read_tree_from_file(file)
    return arbre_nom_num

tree = loadtree()

if __name__ == "__main__":
    arbre = ArbreBinaire("racine", 50)
    a = [chr(random.randint(97 , 122)) for i in range(10)]
    for i in range(10):
        inserer_abr(a[i], i,arbre)

    with open('tree.txt', 'w') as file:
        write_tree_to_file(arbre, file)

    with open('tree.txt', 'r') as file:
        arbre_nom_num = read_tree_from_file(file)
    parcours_infixe_decroissant(arbre_nom_num)