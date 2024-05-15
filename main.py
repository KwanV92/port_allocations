""" Main """

import sys
import time

import pandas as pd

sys.path.insert(
    0,
    "C:/Users/S084870/OneDrive - Abeille Assurances/Bureau/TOM/Projet/port_allocation/port_allocations",
)

from test.computationals import (  # noqa: E402
    compute_all_possible_allocations,
    compute_all_possible_weights,
    test_validity_df,
)


def main() -> None:
    """Main"""
    # TODO

    # 1 - Read constraints file
    dataframe = pd.read_csv("input/constraints.csv")
    test_validity_df(dataframe)
    # 2 - Compute number of possible allocation
    all_possible_weights: list = compute_all_possible_weights(dataframe)
    all_valid_allocations_df: pd.DataFrame = compute_all_possible_allocations(
        dataframe, all_possible_weights
    )
    # 2 bis - print number of allocations
    print(
        "There is",
        all_valid_allocations_df[all_valid_allocations_df.columns[0]].count(),
        "valid allocations",
    )
    # 3 - Write result in output file
    all_valid_allocations_df.to_csv(
        "output/allocations.csv",
        sep=",",
    )


if __name__ == "__main__":
    # Start timer
    start_time: float = time.perf_counter()
    start_time_cpu: float = time.process_time()

    main()

    # End timer
    elapsed_time: float = time.perf_counter() - start_time
    cpu_time: float = time.process_time() - start_time_cpu

    print("\n******** TIME ************")
    print(f"Execution time : {time.strftime('%H:%M:%S', time.gmtime(elapsed_time))}")
    print(f"CPU time : {time.strftime('%H:%M:%S', time.gmtime(cpu_time))}")
