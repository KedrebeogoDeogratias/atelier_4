# -*- coding: utf-8 -*-
import random

def extract_elements_list(lst, nb_to_extract):

    """
    Retourne une sous-liste composée de n éléments choisis aléatoirement
    dans la liste donnée, sans modifier la liste de départ.
    """

    if not lst:
        print("La liste ne doit pas être vide.")

    if nb_to_extract > len(lst):
        print("Impossible d'extraire plus d'éléments que la taille de la liste.")

    # Copie de la liste pour ne pas la modifier
    temp_list = lst.copy()
    extracted = []

    for _ in range(nb_to_extract):
        index = random.randrange(len(temp_list))
        extracted.append(temp_list[index])
        # Supprimer pour éviter les doublons
        temp_list.pop(index)

    return extracted


# Test du code
lst_sorted = [i for i in range(10)]
print('Liste de départ', lst_sorted)
sublist = extract_elements_list(lst_sorted, 5)
print('La sous-liste extraite est', sublist)
print('Liste de départ après appel de la fonction est', lst_sorted)
