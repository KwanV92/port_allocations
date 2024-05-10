""" Main """


import time


def main() -> None:
    """Main"""
    # TODO
    # 1 - Read constraints file
    # 2 - Compute number of possible allocation
    # 3 - Write result in output file
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
    print("**************************")
