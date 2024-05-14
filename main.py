""" Main """

import sys
import time

sys.path.insert(
    0,
    "C:/Users/S084870/OneDrive - Abeille Assurances/Bureau/TOM/Projet/port_allocation/port_allocations",
)

from test.computationals import (  # noqa: E402
    compute_possible_allocations,
    open_csv_to_dataframe,
    test_validity_csv,
)


def main() -> None:
    """Main"""
    # TODO

    # 1 - Read constraints file
    dataFrame = open_csv_to_dataframe(
        "C:/Users/S084870/OneDrive - Abeille Assurances/Bureau/TOM/Projet/port_allocation/port_allocations/input/constraints.csv"
    )
    test_validity_csv(dataFrame)
    # 2 - Compute number of possible allocation & print number of allocations
    # 3 - Write result in output file
    compute_possible_allocations(dataFrame)


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
