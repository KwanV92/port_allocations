import sys

import pandas as pd

sys.path.insert(
    0,
    "C:/Users/S084870/OneDrive - Abeille Assurances/Bureau/TOM/Projet/port_allocation/port_allocations",
)


def create_dico(keys: list, values: list) -> dict:
    dico = {
        keys: values  # on associe la clé à la valeur
        for keys, values in zip(
            keys, values
        )  # pour chaque valeur des 2 listes, en utilisant zip() pour parcourir les 2 à la fois
    }
    return dico


def sum_from_tuple(t: tuple) -> int:
    sum = 0
    for item in t:
        sum = sum + item

    return sum


def list_slicer(list: list):
    for object in list:
        yield tuple(object)


def open_csv_to_dataframe(filename: str) -> pd.DataFrame:
    df = pd.read_csv("constraints.csv")
    return df
