""" Main """
import os
import sys
import time

sys.path.insert(
    0,
    "C:/Users/S084870/OneDrive - Abeille Assurances/Bureau/TOM/Projet/port_allocation/port_allocations",
)

from computationals import (  # noqa: E402
    compute_all_allocations,
    csv_reader,
    write_all_allocations,
)
from helper import create_dico  # noqa: E402

os.chdir(
    "C:/Users/S084870/OneDrive - Abeille Assurances/Bureau/TOM/Projet/port_allocation/port_allocations"
)


def main() -> None:
    """Main"""
    # TODO
    # 1 - Read constraints file
    assets, steps = csv_reader("constraints.csv")
    dico = create_dico(assets, steps)
    print(dico)
    # 2 - Compute number of possible allocation & print number of allocations
    compute_all_allocations(assets, steps)
    # 3 - Write result in output file
    write_all_allocations(assets, steps)
    # 4 - Test with several constraints files


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
