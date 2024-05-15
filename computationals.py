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


def test_validity_df(df: pd.DataFrame):
    """Test if the column UNDERLYINGS is present and then if the rows in that column are named MIN_EXPO, MAX_EXPO, and STEP

    The test operates by firstly checking if the column UNDERLYINGS exist, and then if the terms MIN_EXPO, MAX_EXPO, and STEP are in the column

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame created from the constraints CSV

    Raises
    -------
    Exception
        Because the column UNDERLYINGS or the rows MIN_EXPO, MAX_EXPO, and STEP don't exist in the DataFrame

    See Also
    --------
    df.columns, df.values

    References
    ----------
        [1] The official pandas website : https://pandas.pydata.org/
        [2] Multiple pages of the StackOverflow websites : https://stackoverflow.com/
    """

    condition_1: bool = ASSETS in df.columns
    if condition_1:
        print("la colonne", ASSETS, "est présente")
    else:
        raise Exception(
            "Le fichier des contraintes nest pas valide, assurez-vous que la colonne",
            ASSETS,
            "est bien présente",
        )
    condition_2: bool = MIN_EXPO in df[ASSETS].values
    condition_3: bool = MAX_EXPO in df[ASSETS].values
    condition_4: bool = STEP in df[ASSETS].values
    if condition_2 and condition_3 and condition_4:
        print("Le fichier des contraintes est valide")
    else:
        raise Exception(
            "Le fichier des contraintes nest pas valide, assurez-vous que",
            MIN_EXPO,
            MAX_EXPO,
            "et",
            STEP,
            "sont bien le nom des lignes.",
        )


def assign_row_to_variable(df: pd.DataFrame) -> tuple:
    """Assign the rows of the constraints DataFrame to variables"

    Extract the rows MIN_EXPO, MAX_EXPO, and STEP using pandas, and assign them to 3 NumPy arrays named min_expo, max_expo, steps.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame created from the constraints CSV

    Returns
    -------
    min_expo : NumPy.array
        An array composed of the minimal exposition of every asset
    max_expo : NumPy.array
        An array composed of the maximal exposition of every asset
    steps : NumPy.array
        An array composed of the step of every asset

    See Also
    --------
    df.loc

    References
    ----------
        [1] The official NumPy website : https://numpy.org/
        [2] Multiple pages of the StackOverflow websites : https://stackoverflow.com/
    """

    df.set_index(ASSETS, inplace=True)
    min_expo: np.ndarray = np.array(df.loc[MIN_EXPO])
    max_expo: np.ndarray = np.array(df.loc[MAX_EXPO])
    steps: np.ndarray = np.array(df.loc[STEP])
    return (min_expo, max_expo, steps)


def compute_all_possible_weights(df: pd.DataFrame) -> list:
    """Compute all the possible weight for all the assets

    Assign 3 arrays, min_expo, max_expo and steps, using assign_row_to_variable, and compute all the possible weight of every asset.
    Then return a list containing n-lists made of every weight from the n-assets

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame created from the constraints CSV

    Returns
    -------
    all_assets_possible_weights: list
        List made of n-lists containing each every weight from an asset

    See Also
    --------
    assign_row_to_variable
    enumerate
    np.arrange

    References
    ----------
        [1] The official NumPy website : https://numpy.org/
        [2] Multiple pages of the StackOverflow websites : https://stackoverflow.com/
    """

    all_assets_possible_weights: list[list] = []
    min_expo, max_expo, steps = assign_row_to_variable(df)
    for index, item in enumerate(steps):
        asset_possible_weights: np.ndarray = np.arange(
            start=min_expo[index], stop=max_expo[index], step=item, dtype=int
        )
        all_assets_possible_weights.append(list(asset_possible_weights))
    return all_assets_possible_weights


def compute_all_possible_allocations(
    df: pd.DataFrame, detailed_weights: list
) -> pd.DataFrame:
    """Compute all the valid allocations all every assets

    Firstly, create a DataFrame to store inside all the valid allocations (the sum of the weight of every asset is equal to 100).
    Secondly, compute all the possible combination of every weight of the assets. Only keep the valid ones, to put them in the new DataFrame.
    Finally, change the index of the new DataFrame to the number of the valid allocation

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame created from the constraints CSV
    detailed_weights: list
        List made of n-lists containing each every weight from an assets

    Returns
    -------
    allocations_df: pandas.DataFrame
        The new DataFrame which has the asstes name as the header and containing all the valid allocations

    See Also
    --------
    pandas.DataFrame
    product
    sum_from_tuple
    df.loc
    df.set_index
    df.iloc

    References
    ----------
        [1] The official NumPy website : https://numpy.org/
        [2] The official pandas website : https://pandas.pydata.org/
        [3] Multiple pages of the StackOverflow websites : https://stackoverflow.com/
    """
    # on garde seulement la liste des actifs en enlevant
    df_header = "allocation number" + pd.DataFrame(columns=df.columns)
    allocations_df: pd.DataFrame = df_header
    number_of_allocations: int = 0
    for combination in product(*detailed_weights):
        if sum_from_tuple(combination) == 100:
            number_of_allocations = number_of_allocations + 1
            new_row: list = list(combination)
            row_number: str = "N°" + str(number_of_allocations)
            allocations_df.loc[row_number] = new_row
    allocations_df.set_index(allocations_df.iloc[:, 0], inplace=True)
    return allocations_df
