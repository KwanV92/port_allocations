import sys

import pandas as pd
import pytest

sys.path.insert(
    0,
    "C:/Users/S084870/OneDrive - Abeille Assurances/Bureau/TOM/Projet/port_allocation/port_allocations",
)
from src.computationals import (  # noqa: E402
    check_validity_df,
    compute_all_possible_allocations,
    compute_all_possible_weights,
)

df_basic = pd.read_csv("input/constraints.csv")

df_empty = pd.DataFrame()


def test_check_validity_df_empty():
    with pytest.raises(Exception):
        check_validity_df(df_empty)


df_error_ASSETS = pd.read_csv("testing/constraints_error_ASSETS.csv")


def test_check_validity_df_error_ASSETS():
    with pytest.raises(Exception):
        check_validity_df(df_error_ASSETS)


df_error_MIN_EXPO = pd.read_csv("testing/constraints_error_MIN_EXPO.csv")


def test_check_validity_df_error_MIN_EXPO():
    with pytest.raises(Exception):
        check_validity_df(df_error_MIN_EXPO)


df_error_MAX_EXPO = pd.read_csv("testing/constraints_error_MAX_EXPO.csv")


def test_check_validity_df_error_MAX_EXPO():
    with pytest.raises(Exception):
        check_validity_df(df_error_MAX_EXPO)


df_error_STEP = pd.read_csv("testing/constraints_error_STEP.csv")


def test_check_validity_df_error_STEP():
    with pytest.raises(Exception):
        check_validity_df(df_error_STEP)


list_test = []

compute_all_possible_allocations(df_error_MIN_EXPO, list_test)


def test_compute_all_possible_allocations_empty_df():
    with pytest.raises(IndexError):
        compute_all_possible_allocations(df_empty, list_test)


df_classic = pd.read_csv("input/constraints.csv")


def test_compute_all_possible_weights_and_allocations_classic_df():
    list_of_weights = compute_all_possible_weights(df_classic)
    final_df = compute_all_possible_allocations(df_classic, list_of_weights)
    assert final_df.shape[0] == 10626
    assert final_df.shape[1] == 5
    assert len(list_of_weights) == 5
    assert len(list_of_weights[0]) == 21


df_4step = pd.read_csv("input/constraints_2.csv")


def test_compute_all_possible_weights_and_allocations_4step_df():
    list_of_weights = compute_all_possible_weights(df_4step)
    final_df = compute_all_possible_allocations(df_4step, list_of_weights)
    assert final_df.shape[0] == 23751
    assert final_df.shape[1] == 5
    assert len(list_of_weights) == 5
    assert len(list_of_weights[0]) == 26


df_100step = pd.read_csv("input/constraints_3.csv")


def test_compute_all_possible_weights_and_allocations_100step_df():
    list_of_weights = compute_all_possible_weights(df_100step)
    final_df = compute_all_possible_allocations(df_100step, list_of_weights)
    assert final_df.shape[0] == 5
    assert final_df.shape[1] == 5
    assert len(list_of_weights) == 5
    assert len(list_of_weights[0]) == 2
