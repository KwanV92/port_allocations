import os
import sys

sys.path.insert(
    0,
    "C:/Users/S084870/OneDrive - Abeille Assurances/Bureau/TOM/Projet/port_allocation/port_allocations",
)


os.chdir(
    "C:/Users/S084870/OneDrive - Abeille Assurances/Bureau/TOM/Projet/port_allocation/port_allocations"
)


def create_dico(keys: list, values: list) -> dict:
    dico = {
        keys: values  # on associe la clé à la valeur
        for keys, values in zip(
            keys, values
        )  # pour chaque valeur des 2 listes, en utilisant zip() pour parcourir les 2 à la fois
    }
    return dico


def somme(a: float, b: float) -> str:
    x: float = a + b

    return str(x)


def somme_from_list(t: tuple) -> int:
    res = 0
    for item in t:
        res = res + item

    return res


def list_slicer(list: list):
    for object in list:
        yield tuple(object)
