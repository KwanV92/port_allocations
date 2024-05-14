import sys
from itertools import product

import numpy as np
import pandas as pd

sys.path.insert(
    0,
    "C:/Users/S084870/OneDrive - Abeille Assurances/Bureau/TOM/Projet/port_allocation/port_allocations",
)


from test.constants import ASSETS, MAX_EXPO, MIN_EXPO, STEP  # noqa: F403, E402
from test.helper import sum_from_tuple  # noqa: E402


def test_validity_csv(df: pd.DataFrame):
    condition_1: bool = MIN_EXPO in df[ASSETS].values
    condition_2: bool = MAX_EXPO in df[ASSETS].values
    condition_3: bool = STEP in df[ASSETS].values
    if (condition_1 is False) or (condition_2 is False) or (condition_3 is False):
        raise Exception(
            "Le fichier des contraintes nest pas valide, assurez-vous que",
            MIN_EXPO,
            MAX_EXPO,
            "et",
            STEP,
            "sont bien le nom des lignes.",
        )
    else:
        print("Le fichier des contraintes est valide")


def open_csv_to_dataframe(filename: str) -> pd.DataFrame:
    df = pd.read_csv(filename)
    return df


def assign_row_to_variable(df: pd.DataFrame) -> tuple:
    min_expo: np.ndarray = np.array(df.loc[df["UNDERLYINGS"] == MIN_EXPO])
    min_expo = np.delete(min_expo, 0)
    max_expo: np.ndarray = np.array(df.loc[df["UNDERLYINGS"] == MAX_EXPO])
    max_expo = np.delete(max_expo, 0)
    steps: np.ndarray = np.array(df.loc[df["UNDERLYINGS"] == STEP])
    steps = np.delete(steps, 0)
    return (min_expo, max_expo, steps)


def compute_possible_steps(df: pd.DataFrame) -> list:
    detailled_weight: list = []
    min_expo, max_expo, steps = assign_row_to_variable(df)
    for index, step in enumerate(steps):
        asset_possible_weight: list = []
        asset_weight: int = min_expo[index]
        while asset_weight <= max_expo[index]:
            asset_possible_weight.append(asset_weight)
            asset_weight = asset_weight + step
        detailled_weight.append(asset_possible_weight)
    return detailled_weight


def compute_possible_allocations(df: pd.DataFrame) -> None:
    assets: tuple = tuple(df.iloc[1].index[1:])
    allocations_df: pd.DataFrame = pd.DataFrame(columns=assets)
    detailed_steps: list = compute_possible_steps(df)
    row_index: int = 0
    for assets in product(*detailed_steps):
        if sum_from_tuple(assets) == 100:
            new_row: list = list(assets)
            allocations_df.loc[row_index] = new_row
            row_index = row_index + 1
    return allocations_df.to_csv(
        "C:/Users/S084870/OneDrive - Abeille Assurances/Bureau/TOM/Projet/port_allocation/port_allocations/output/allocations.csv",
        sep=",",
    )


df = open_csv_to_dataframe(
    "C:/Users/S084870/OneDrive - Abeille Assurances/Bureau/TOM/Projet/port_allocation/port_allocations/input/constraints.csv"
)
