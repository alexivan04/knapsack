import os
import time
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np  # for trendline calculation
import heapq

class Poz:
    def __init__(self, g, c):
        self.g = g  # Weight
        self.c = c  # Value

def knapsack_dynamic(n, G, a):
    C = [[0] * (G + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, G + 1):
            if a[i - 1].g <= j and a[i - 1].c + C[i - 1][j - a[i - 1].g] > C[i - 1][j]:
                C[i][j] = a[i - 1].c + C[i - 1][j - a[i - 1].g]
            else:
                C[i][j] = C[i - 1][j]
    
    return C[n][G]  # Return the optimal value

def knapsack_backtracking(n, W, items):
    # Helper function to explore possible solutions
    def backtrack(i, remaining_weight, current_value):
        nonlocal best_value

        # If all items have been considered, return the best value found
        if i == n:
            best_value = max(best_value, current_value)
            return

        # If the current item can fit, try including it
        if items[i].g <= remaining_weight:  # Access weight using .g
            backtrack(i + 1, remaining_weight - items[i].g, current_value + items[i].c)  # Access value using .c

        # Try excluding the current item
        backtrack(i + 1, remaining_weight, current_value)

    best_value = 0
    backtrack(0, W, 0)  # Start from the first item with full capacity and value 0
    return best_value


class Poz:
    def __init__(self, g, c):
        self.g = g  # weight
        self.c = c  # value

class Node:
    def __init__(self, level, value, weight, bound):
        self.level = level  # current level (item index)
        self.value = value  # value of the current node
        self.weight = weight  # weight of the current node
        self.bound = bound  # upper bound of the solution

    # For heapq priority queue (to sort by bound)
    def __lt__(self, other):
        return self.bound > other.bound  # We want higher bound first

def knapsack_branch_bound(n, G, items):
    def calculate_bound(node, n, G, items):
        if node.weight >= G:
            return 0  # Can't take more items if the weight exceeds the capacity

        bound = node.value
        total_weight = node.weight
        level = node.level + 1

        # Take as many items as possible within the capacity
        while level < n and total_weight + items[level].g <= G:
            total_weight += items[level].g
            bound += items[level].c
            level += 1

        # If there are items left, we take a fraction of the next item (fractional knapsack bound)
        if level < n:
            bound += (G - total_weight) * items[level].c / items[level].g  # Fraction of the next item

        return bound

    # Priority Queue (min-heap), we use negative bound for max-heap behavior
    pq = []
    root = Node(-1, 0, 0, 0)
    root.bound = calculate_bound(root, n, G, items)

    heapq.heappush(pq, root)

    max_value = 0

    while pq:
        node = heapq.heappop(pq)

        # If we reach a leaf node, check if it's the best solution
        if node.level == n - 1:
            continue

        # Consider the left child (including the item)
        next_level = node.level + 1
        if node.weight + items[next_level].g <= G:
            left_value = node.value + items[next_level].c
            left_weight = node.weight + items[next_level].g
            left_bound = calculate_bound(Node(next_level, left_value, left_weight, 0), n, G, items)

            if left_bound > max_value:
                max_value = left_value
                heapq.heappush(pq, Node(next_level, left_value, left_weight, left_bound))

        # Consider the right child (excluding the item)
        right_bound = calculate_bound(Node(next_level, node.value, node.weight, 0), n, G, items)
        if right_bound > max_value:
            heapq.heappush(pq, Node(next_level, node.value, node.weight, right_bound))

    return max_value


def solve_test_case(file_path):
    """
    Solve a single test case from a file using Dynamic Programming, Backtracking, and Branch and Bound.

    :param file_path: Path to the test case file
    :return: (number of items, knapsack capacity, execution time for each method)
    """
    with open(file_path, "r") as f:
        # Read number of items and knapsack capacity
        n, G = map(int, f.readline().split())
        a = []

        # Read the items
        for _ in range(n):
            g, c = map(int, f.readline().split())
            a.append(Poz(g, c))

    # Measure execution time for Dynamic Programming
    start_time = time.time()
    dp_result = knapsack_dynamic(n, G, a)
    dp_time = (time.time() - start_time) * 10000  # Convert to nanoseconds

    # Measure execution time for Backtracking
    start_time = time.time()
    backtracking_result = knapsack_backtracking(n, G, a)
    backtracking_time = (time.time() - start_time) * 10000  # Convert to nanoseconds

    # Measure execution time for Branch and Bound
    start_time = time.time()
    branch_bound_result = knapsack_branch_bound(n, G, a)
    branch_bound_time = (time.time() - start_time) * 10000  # Convert to nanoseconds

    # Output the results
    print(f"Result for {file_path}: DP: {dp_result}, Backtracking: {backtracking_result}, Branch and Bound: {branch_bound_result}")
    print(f"Execution Times: DP: {dp_time:.3f} ns, Backtracking: {backtracking_time:.3f} ns, Branch and Bound: {branch_bound_time:.3f} ns")

    return n, G, dp_time, backtracking_time, branch_bound_time


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
    df_category1 = pd.DataFrame(results_category1, columns=["Number of Items", "Knapsack Capacity", "DP Execution Time (ns)", "Backtracking Execution Time (ns)", "Branch and Bound Execution Time (ns)"])
    df_category2 = pd.DataFrame(results_category2, columns=["Number of Items", "Knapsack Capacity", "DP Execution Time (ns)", "Backtracking Execution Time (ns)", "Branch and Bound Execution Time (ns)"])

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

    # Plot the results for Dynamic Programming (Category 1)
    plt.figure(figsize=(10, 6), dpi=150)
    plt.scatter(df_category1["Number of Items"], df_category1["DP Execution Time (ns)"], marker="o", color="blue", s=30, label="DP Execution Time")
    plt.title("Dynamic Programming Execution Time vs Number of Items (Category 1)")
    plt.xlabel("Number of Items")
    plt.ylabel("Execution Time (ns)")
    plt.grid(True)
    plt.legend()
    dp_plot_path_category1 = os.path.join(outputs_dir, "DP_execution_time_vs_items_category1.png")
    plt.savefig(dp_plot_path_category1, dpi=150)
    print(f"DP Plot for category 1 saved to {dp_plot_path_category1}")
    plt.close()

    # Plot the results for Backtracking (Category 1)
    plt.figure(figsize=(10, 6), dpi=150)
    plt.scatter(df_category1["Number of Items"], df_category1["Backtracking Execution Time (ns)"], marker="o", color="red", s=30, label="Backtracking Execution Time")
    plt.title("Backtracking Execution Time vs Number of Items (Category 1)")
    plt.xlabel("Number of Items")
    plt.ylabel("Execution Time (ns)")
    plt.grid(True)
    plt.legend()
    backtracking_plot_path_category1 = os.path.join(outputs_dir, "Backtracking_execution_time_vs_items_category1.png")
    plt.savefig(backtracking_plot_path_category1, dpi=150)
    print(f"Backtracking Plot for category 1 saved to {backtracking_plot_path_category1}")
    plt.close()

    # Plot the results for Branch and Bound (Category 1)
    plt.figure(figsize=(10, 6), dpi=150)
    plt.scatter(df_category1["Number of Items"], df_category1["Branch and Bound Execution Time (ns)"], marker="o", color="green", s=30, label="Branch and Bound Execution Time")
    plt.title("Branch and Bound Execution Time vs Number of Items (Category 1)")
    plt.xlabel("Number of Items")
    plt.ylabel("Execution Time (ns)")
    plt.grid(True)
    plt.legend()
    branch_bound_plot_path_category1 = os.path.join(outputs_dir, "Branch_and_Bound_execution_time_vs_items_category1.png")
    plt.savefig(branch_bound_plot_path_category1, dpi=150)
    print(f"Branch and Bound Plot for category 1 saved to {branch_bound_plot_path_category1}")
    plt.close()

    # Plot the results for Dynamic Programming (Category 2)
    plt.figure(figsize=(10, 6), dpi=150)
    plt.scatter(df_category2["Knapsack Capacity"], df_category2["DP Execution Time (ns)"], marker="o", color="blue", s=30, label="DP Execution Time")
    plt.title("Dynamic Programming Execution Time vs Knapsack Capacity (Category 2)")
    plt.xlabel("Knapsack Capacity")
    plt.ylabel("Execution Time (ns)")
    plt.grid(True)
    plt.legend()
    dp_plot_path_category2 = os.path.join(outputs_dir, "DP_execution_time_vs_capacity_category2.png")
    plt.savefig(dp_plot_path_category2, dpi=150)
    print(f"DP Plot for category 2 saved to {dp_plot_path_category2}")
    plt.close()

    # Plot the results for Backtracking (Category 2)
    plt.figure(figsize=(10, 6), dpi=150)
    plt.scatter(df_category2["Knapsack Capacity"], df_category2["Backtracking Execution Time (ns)"], marker="o", color="red", s=30, label="Backtracking Execution Time")
    plt.title("Backtracking Execution Time vs Knapsack Capacity (Category 2)")
    plt.xlabel("Knapsack Capacity")
    plt.ylabel("Execution Time (ns)")
    plt.grid(True)
    plt.legend()
    backtracking_plot_path_category2 = os.path.join(outputs_dir, "Backtracking_execution_time_vs_capacity_category2.png")
    plt.savefig(backtracking_plot_path_category2, dpi=150)
    print(f"Backtracking Plot for category 2 saved to {backtracking_plot_path_category2}")
    plt.close()

    # Plot the results for Branch and Bound (Category 2)
    plt.figure(figsize=(10, 6), dpi=150)
    plt.scatter(df_category2["Knapsack Capacity"], df_category2["Branch and Bound Execution Time (ns)"], marker="o", color="green", s=30, label="Branch and Bound Execution Time")
    plt.title("Branch and Bound Execution Time vs Knapsack Capacity (Category 2)")
    plt.xlabel("Knapsack Capacity")
    plt.ylabel("Execution Time (ns)")
    plt.grid(True)
    plt.legend()
    branch_bound_plot_path_category2 = os.path.join(outputs_dir, "Branch_and_Bound_execution_time_vs_capacity_category2.png")
    plt.savefig(branch_bound_plot_path_category2, dpi=150)
    print(f"Branch and Bound Plot for category 2 saved to {branch_bound_plot_path_category2}")
    plt.close()

if __name__ == "__main__":
    main()



if __name__ == "__main__":
    main()
