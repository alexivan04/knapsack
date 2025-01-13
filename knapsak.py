import os
import time
import matplotlib.pyplot as plt
import pandas as pd

class Poz:
    def __init__(self, g, c):
        self.g = g
        self.c = c

def dinamica(n, G, a):
    # Initialize the DP table with zeros
    C = [[0] * (G + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, G + 1):
            if a[i - 1].g <= j and a[i - 1].c + C[i - 1][j - a[i - 1].g] > C[i - 1][j]:
                C[i][j] = a[i - 1].c + C[i - 1][j - a[i - 1].g]
            else:
                C[i][j] = C[i - 1][j]
    
    return C

def solve_test_case(file_path):
    """
    Solve a single test case from a file.

    :param file_path: Path to the test case file
    :return: (number of items, knapsack capacity, execution time)
    """
    with open(file_path, "r") as f:
        # Read number of items and knapsack capacity
        n, G = map(int, f.readline().split())
        a = []

        # Read the items
        for _ in range(n):
            g, c = map(int, f.readline().split())
            a.append(Poz(g, c))

    # Measure execution time
    start_time = time.time()
    C = dinamica(n, G, a)
    end_time = time.time()

    execution_time = end_time - start_time

    # Output the result
    print(f"Result for {file_path}: {C[n][G]} (Execution Time: {execution_time:.6f} seconds)")

    return n, G, execution_time

def main():
    """
    Main function to process all test cases in the 'tests' directory and plot results.
    """
    test_dir = "tests"
    results = []

    # Ensure the test directory exists
    if not os.path.exists(test_dir):
        print(f"Test directory '{test_dir}' not found.")
        return

    # Process each test case file
    for test_file in sorted(os.listdir(test_dir)):
        if test_file.endswith(".txt"):
            file_path = os.path.join(test_dir, test_file)
            results.append(solve_test_case(file_path))

    # Create a DataFrame for the results
    df = pd.DataFrame(results, columns=["Number of Items", "Knapsack Capacity", "Execution Time (s)"])

    # Save the results to an Excel file
    excel_path = "results.xlsx"
    df.to_excel(excel_path, index=False)
    print(f"Results saved to {excel_path}")

    # Plot the results
    plt.figure(figsize=(10, 6))

    # Plot execution time vs number of items
    plt.plot(df["Number of Items"], df["Execution Time (s)"], marker="o", label="Execution Time")
    plt.title("Execution Time vs Number of Items")
    plt.xlabel("Number of Items")
    plt.ylabel("Execution Time (seconds)")
    plt.legend()
    plt.grid()

    # Save the plot
    plot_path = "execution_time_plot.png"
    plt.savefig(plot_path)
    print(f"Plot saved to {plot_path}")

    # Show the plot
    plt.show()

if __name__ == "__main__":
    main()
