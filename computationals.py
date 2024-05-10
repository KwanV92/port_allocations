import csv
import os
import sys
from itertools import product

sys.path.insert(
    0,
    "C:/Users/S084870/OneDrive - Abeille Assurances/Bureau/TOM/Projet/port_allocation/port_allocations",
)

from helper import somme_from_list  # noqa: E402

os.chdir(
    "C:/Users/S084870/OneDrive - Abeille Assurances/Bureau/TOM/Projet/port_allocation/port_allocations"
)


def all_steps(step: int) -> list:
    res: list = []
    acc: int = 0
    while acc <= 100:
        res.append(acc)
        acc = acc + step
    return res


def list_slicer_for_product(list: list):
    for under_list in list:
        for item in under_list:
            yield item


def csv_reader(doc: str) -> tuple:
    assets: list = []
    steps: list = []
    with open(doc, "r") as file:
        table = csv.reader(file, delimiter=",")
        for index, row in enumerate(table):
            if index == 0:
                for index2, column in enumerate(row):
                    if index2 > 0:
                        assets.append(column)
            if index == 3:
                for index3, column in enumerate(row):
                    if index3 > 0:
                        steps.append(all_steps(int(column)))
    return assets, steps


def compute_all_allocations(assets: list, steps: list) -> None:
    assets_as_tuple: tuple = tuple(assets)
    numbers_of_compute = 0
    for assets_as_tuple in product(*steps):
        if somme_from_list(assets_as_tuple) == 100:
            numbers_of_compute = numbers_of_compute + 1
            print(assets_as_tuple)
    print(numbers_of_compute)


def write_all_allocations(assets: list, steps: list):
    filename = "allocations.csv"
    with open(filename, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=",")
        csvwriter.writerow(assets)
        assets_as_tuple: tuple = tuple(assets)
        for assets_as_tuple in product(*steps):
            if somme_from_list(assets_as_tuple) == 100:
                csvwriter.writerow(assets_as_tuple)
