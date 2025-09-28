# -*- coding: utf-8 -*-


import random

def choose_element_list(lst_sorted):

    if not lst_sorted:
        return print("La liste ne doit pas être vide.")

    return lst_sorted[random.randint(0,len(lst_sorted)-1)]


# Test de votre code 
lst_sorted = [i for i in range(10)]
print('Liste triée de départ',lst_sorted) 
e1 = choose_element_list(lst_sorted) 
print('A la première exécution',e1,'a été sélectionné') 
e2 = choose_element_list(lst_sorted) 
print('A la deuxième exécution',e2,'a été sélectionné') 
assert e1 != e2,"Attention vérifiez votre code, pour deux sélections de suite l'élément sélectionné est le même !"