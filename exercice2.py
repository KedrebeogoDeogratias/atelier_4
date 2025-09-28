import random

def mix_list(list_to_mix):

    """
    Retourne une copie mélangée de list_to_mix sans modifier l'originale.
    """
    # On fait une copie de la liste originale

    mixed = list_to_mix[:]

    # Mélange "à la main" (Fisher-Yates / Knuth shuffle)
    for i in range(len(mixed)-1, 0, -1):
        j = random.randint(0, i)
        mixed[i], mixed[j] = mixed[j], mixed[i]

    return mixed



# --- Test ---
lst_sorted = [i for i in range(10)]
print("Liste triee de depart :", lst_sorted)

mixed_list = mix_list(lst_sorted)
print("Liste melangee obtenue :", mixed_list)
print("Liste triee de depart apres appel a mix_list (doit etre inchangee) :", lst_sorted)

# Vérifications
assert lst_sorted != mixed_list, "Les deux listes doivent être differentes après l'appel a mix_list..."
assert sorted(lst_sorted) == sorted(mixed_list), "Les deux listes doivent contenir les mêmes elements."
