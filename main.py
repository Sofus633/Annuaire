from settings import *

pygame.init()
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

def rechercher_numero(nom, abr_annuaire):
    """ Recherche le numéro qui correspond à un nom.
        Renvoie le numéro recherché si le nom existe, None sinon.
    """
    ...
    
def parcinfixe_avb(node, tab,x=0, y=50):

    if node != None:
        
        parcinfixe_avb(node.gauche,  tab,x, y)

        parcinfixe_avb(node.droite, tab, x, y)
        

def display_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.nom))
        if node.gauche or node.droite:  # Only proceed if there are children
            display_tree(node.gauche, level + 1, "L--- ")
            display_tree(node.droite, level + 1, "R--- ")

def parcours_infixe_decroissant(abr):
    if abr is not None:
        # Visiter le sous-arbre abr
        parcours_infixe_decroissant(abr.droite)
        # Visiter le nœud courant
        print(abr.nom, abr.numero)
        # Visiter le sous-arbre gauche
        parcours_infixe_decroissant(abr.gauche)

def write_tree_to_file(node, file):
    if node is not None:
        file.write(str(node.nom) + ' ' + str(node.numero) + '\n')
        write_tree_to_file(node.gauche, file)
        write_tree_to_file(node.droite, file)

if __name__ == "__main__":
    arbre1 = None
    a = [8, 1, 4, 3, 9, 5, 10, 22, 59, 2, 3, 5]
    for val in a:
        arbre1 = inserer_abr(val, val*100, arbre1)
        


    # Assuming `root` is the root node of the binary tree
    with open('tree.txt', 'w') as file:
        write_tree_to_file(arbre1, file)


