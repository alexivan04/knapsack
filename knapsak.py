import os
import time
import matplotlib.pyplot as plt
import pandas as pd

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
    def backtrack(i, remaining_weight, current_value):
        nonlocal best_value

        if i == n:
            best_value = max(best_value, current_value)
            return

        if items[i].g <= remaining_weight:
            backtrack(i + 1, remaining_weight - items[i].g, current_value + items[i].c)

        backtrack(i + 1, remaining_weight, current_value)

    best_value = 0
    backtrack(0, W, 0)
    return best_value

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

def fractional_knapsack(n, capacity, items):
    items.sort(key=lambda x: x.value / x.weight, reverse=True)

    total_value = 0.0
    for item in items:
        if capacity >= item.weight:
            total_value += item.value
            capacity -= item.weight
        else:
            total_value += (capacity / item.weight) * item.value
            break

    return total_value

def solve_test_case(file_path):
    with open(file_path, "r") as f:
        n, G = map(int, f.readline().split())
        a = []
        for _ in range(n):
            g, c = map(int, f.readline().split())
            a.append(Poz(g, c))

    start_time = time.time()
    dp_result = knapsack_dynamic(n, G, a)
    dp_time = (time.time() - start_time) * 10000

    start_time = time.time()
    backtracking_result = knapsack_backtracking(n, G, a)
    backtracking_time = (time.time() - start_time) * 10000

    start_time = time.time()
    fractional_result = fractional_knapsack(n, G, [Item(x.g, x.c) for x in a])
    fractional_time = (time.time() - start_time) * 10000

    print(f"Result for {file_path}: DP: {dp_result}, Backtracking: {backtracking_result}, Fractional: {fractional_result:.2f}")
    print(f"Execution Times: DP: {dp_time:.3f} ns, Backtracking: {backtracking_time:.3f} ns, Fractional: {fractional_time:.3f} ns")

    return n, G, dp_time, backtracking_time, fractional_time

def main():
    category1_dir = "tests/category1"
    category2_dir = "tests/category2"
    results_category1 = []
    results_category2 = []

    if not os.path.exists(category1_dir) or not os.path.exists(category2_dir):
        print(f"One or both test directories '{category1_dir}' or '{category2_dir}' not found.")
        return

    for test_file in sorted(os.listdir(category1_dir)):
        if test_file.endswith(".txt"):
            file_path = os.path.join(category1_dir, test_file)
            results_category1.append(solve_test_case(file_path))

    for test_file in sorted(os.listdir(category2_dir)):
        if test_file.endswith(".txt"):
            file_path = os.path.join(category2_dir, test_file)
            results_category2.append(solve_test_case(file_path))

    df_category1 = pd.DataFrame(results_category1, columns=["Number of Items", "Knapsack Capacity", "DP Execution Time (ns)", "Backtracking Execution Time (ns)", "Fractional Execution Time (ns)"])
    df_category2 = pd.DataFrame(results_category2, columns=["Number of Items", "Knapsack Capacity", "DP Execution Time (ns)", "Backtracking Execution Time (ns)", "Fractional Execution Time (ns)"])

    outputs_dir = "outputs"
    os.makedirs(outputs_dir, exist_ok=True)

    excel_path_category1 = os.path.join(outputs_dir, "results_category1.xlsx")
    excel_path_category2 = os.path.join(outputs_dir, "results_category2.xlsx")
    df_category1.to_excel(excel_path_category1, index=False)
    df_category2.to_excel(excel_path_category2, index=False)
    print(f"Results for category 1 saved to {excel_path_category1}")
    print(f"Results for category 2 saved to {excel_path_category2}")

    plt.figure(figsize=(10, 6), dpi=150)
    plt.scatter(df_category1["Number of Items"], df_category1["DP Execution Time (ns)"], marker="o", color="blue", s=30, label="DP Execution Time")
    plt.title("Dynamic Programming Execution Time vs Number of Items (Category 1)")
    plt.xlabel("Number of Items")
    plt.ylabel("Execution Time (ns)")
    plt.grid(True)
    plt.legend()
    dp_plot_path_category1 = os.path.join(outputs_dir, "DP_execution_time_vs_items_category1.png")
    plt.savefig(dp_plot_path_category1, dpi=150)
    plt.close()

    plt.figure(figsize=(10, 6), dpi=150)
    plt.scatter(df_category1["Number of Items"], df_category1["Backtracking Execution Time (ns)"], marker="o", color="red", s=30, label="Backtracking Execution Time")
    plt.title("Backtracking Execution Time vs Number of Items (Category 1)")
    plt.xlabel("Number of Items")
    plt.ylabel("Execution Time (ns)")
    plt.grid(True)
    plt.legend()
    backtracking_plot_path_category1 = os.path.join(outputs_dir, "Backtracking_execution_time_vs_items_category1.png")
    plt.savefig(backtracking_plot_path_category1, dpi=150)
    plt.close()

    plt.figure(figsize=(10, 6), dpi=150)
    plt.scatter(df_category1["Number of Items"], df_category1["Fractional Execution Time (ns)"], marker="o", color="green", s=30, label="Fractional Execution Time")
    plt.title("Fractional Knapsack Execution Time vs Number of Items (Category 1)")
    plt.xlabel("Number of Items")
    plt.ylabel("Execution Time (ns)")
    plt.grid(True)
    plt.legend()
    fractional_plot_path_category1 = os.path.join(outputs_dir, "Fractional_execution_time_vs_items_category1.png")
    plt.savefig(fractional_plot_path_category1, dpi=150)
    plt.close()

if __name__ == "__main__":
    main()
