import os
import time
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np  # for trendline calculation

class Poz:
    def __init__(self, g, c):
        self.g = g
        self.c = c

def knapsack(n, G, a):
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
    C = knapsack(n, G, a)
    end_time = time.time()

    execution_time = (end_time - start_time) * 10000 # in nanoseconds

    # Output the result
    print(f"Result for {file_path}: {C[n][G]} (Execution Time: {execution_time:.3f} ms)")

    return n, G, execution_time

def main():
    """
    Main function to process all test cases in the 'tests' directory and plot results.
    """
    # Directories for category 1 and category 2 test cases
    category1_dir = "tests/category1"
    category2_dir = "tests/category2"
    results_category1 = []
    results_category2 = []

    # Ensure the test directories exist
    if not os.path.exists(category1_dir) or not os.path.exists(category2_dir):
        print(f"One or both test directories '{category1_dir}' or '{category2_dir}' not found.")
        return

    # Process each test case file in category 1 (time complexity vs. number of items)
    for test_file in sorted(os.listdir(category1_dir)):
        if test_file.endswith(".txt"):
            file_path = os.path.join(category1_dir, test_file)
            results_category1.append(solve_test_case(file_path))

    # Process each test case file in category 2 (time complexity vs. knapsack capacity)
    for test_file in sorted(os.listdir(category2_dir)):
        if test_file.endswith(".txt"):
            file_path = os.path.join(category2_dir, test_file)
            results_category2.append(solve_test_case(file_path))

    # Create DataFrames for the results
    df_category1 = pd.DataFrame(results_category1, columns=["Number of Items", "Knapsack Capacity", "Execution Time (ms)"])
    df_category2 = pd.DataFrame(results_category2, columns=["Number of Items", "Knapsack Capacity", "Execution Time (ms)"])

    # Sort the data by the relevant columns before saving
    df_category1 = df_category1.sort_values(by=["Number of Items"])  # Sorting by Number of Items for Category 1
    df_category2 = df_category2.sort_values(by=["Knapsack Capacity"])  # Sorting by Knapsack Capacity for Category 2

    # Create the outputs directory if it doesn't exist
    outputs_dir = "outputs"
    os.makedirs(outputs_dir, exist_ok=True)

    # Save the results to Excel files in the outputs folder
    excel_path_category1 = os.path.join(outputs_dir, "results_category1.xlsx")
    excel_path_category2 = os.path.join(outputs_dir, "results_category2.xlsx")
    df_category1.to_excel(excel_path_category1, index=False)
    df_category2.to_excel(excel_path_category2, index=False)
    print(f"Results for category 1 saved to {excel_path_category1}")
    print(f"Results for category 2 saved to {excel_path_category2}")

    # Plot the results for category 1 (time complexity vs number of items)
    plt.figure(figsize=(10, 6), dpi=150)  # Increased DPI for finer graph
    plt.scatter(df_category1["Number of Items"], df_category1["Execution Time (ms)"], marker="o", label="Execution Time", color="blue", s=30)  # Reduced marker size

    # Calculate the trendline using linear regression (polyfit)
    slope, intercept = np.polyfit(df_category1["Number of Items"], df_category1["Execution Time (ms)"], 1)
    trendline = np.polyval([slope, intercept], df_category1["Number of Items"])

    # Plot the trendline
    plt.plot(df_category1["Number of Items"], trendline, color="red", label="Trendline")

    plt.title("Execution Time vs Number of Items (Category 1)")
    plt.xlabel("Number of Items")
    plt.ylabel("Execution Time (ms)")
    plt.legend()
    plt.grid(True)

    # Save the plot for category 1 in the outputs folder
    plot_path_category1 = os.path.join(outputs_dir, "execution_time_vs_items_plot_with_trendline.png")
    plt.savefig(plot_path_category1, dpi=150)  # Save with higher DPI
    print(f"Plot for category 1 with trendline saved to {plot_path_category1}")
    plt.show()

    # Plot the results for category 2 (time complexity vs knapsack capacity)
    plt.figure(figsize=(10, 6), dpi=150)  # Increased DPI for finer graph
    plt.scatter(df_category2["Knapsack Capacity"], df_category2["Execution Time (ms)"], marker="o", label="Execution Time", color="green", s=30)  # Reduced marker size

    # Calculate the trendline using linear regression (polyfit)
    slope, intercept = np.polyfit(df_category2["Knapsack Capacity"], df_category2["Execution Time (ms)"], 1)
    trendline = np.polyval([slope, intercept], df_category2["Knapsack Capacity"])

    # Plot the trendline
    plt.plot(df_category2["Knapsack Capacity"], trendline, color="red", label="Trendline")

    plt.title("Execution Time vs Knapsack Capacity (Category 2)")
    plt.xlabel("Knapsack Capacity")
    plt.ylabel("Execution Time (ms)")
    plt.legend()
    plt.grid(True)

    # Save the plot for category 2 in the outputs folder
    plot_path_category2 = os.path.join(outputs_dir, "execution_time_vs_capacity_plot_with_trendline.png")
    plt.savefig(plot_path_category2, dpi=150)  # Save with higher DPI
    print(f"Plot for category 2 with trendline saved to {plot_path_category2}")
    plt.show()

if __name__ == "__main__":
    main()
