import os
import sys
from itertools import product

import numpy as np
import pandas as pd

sys.path.insert(
    0,
    "C:/Users/S084870/OneDrive - Abeille Assurances/Bureau/TOM/Projet/port_allocation/port_allocations",
)


os.chdir(
    "C:/Users/S084870/OneDrive - Abeille Assurances/Bureau/TOM/Projet/port_allocation/port_allocations"
)
from test.constants import *  # noqa: E402, F403
from test.helper import sum_from_tuple  # noqa: E402


def csv_dataframe(filename: str) -> pd.DataFrame:
    df = pd.read_csv("constraints.csv")
    return df


def compute_possible_steps(df: pd.DataFrame) -> list:
    detailled_steps: list = []
    MIN_EXPO = np.array(df.iloc[0, 1:])
    MAX_EXPO = np.array(df.iloc[1, 1:])
    STEP = np.array(df.iloc[2, 1:])
    for index, step in enumerate(STEP):
        asset_possible_allocation: list = []
        asset_step = MIN_EXPO[index]
        while asset_step <= MAX_EXPO[index]:
            asset_possible_allocation.append(asset_step)
            asset_step = asset_step + step
        detailled_steps.append(asset_possible_allocation)
    return detailled_steps


def compute_possible_allocations(filename: str):
    df = csv_dataframe(filename)
    ASSETS: tuple = tuple(df.iloc[1].index[1:])
    allocations_df = pd.DataFrame(columns=ASSETS)
    detailled_steps = compute_possible_steps(df)
    row_index = 0
    for ASSETS in product(*detailled_steps):
        if sum_from_tuple(ASSETS) == 100:
            new_row = list(ASSETS)
            allocations_df.loc[row_index] = new_row
            row_index = row_index + 1
    allocations_df.to_csv("allocations.csv", sep=",")
