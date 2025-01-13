import random

def generate_knapsack_tests(num_tests=5, max_items=10, max_capacity=50, max_weight=20, max_value=100):
    """
    Generate test cases for the 0/1 Knapsack problem with two categories.

    :param num_tests: Number of test cases to generate
    :param max_items: Maximum number of items per test case
    :param max_capacity: Maximum capacity of the knapsack
    :param max_weight: Maximum weight of an item
    :param max_value: Maximum value of an item
    :return: Tuple of two lists: (category1, category2) where:
             - category1: Test cases with varying `n` and fixed `G`
             - category2: Test cases with varying `G` and fixed `n`
    """
    category1 = []
    category2 = []

    for i in range(1, num_tests + 1):
        # Generate Category 1 (varying n, fixed G)
        n = random.randint(1, max_items)
        G = max_capacity  # Fixed capacity for this category
        items = [(random.randint(1, max_weight), random.randint(1, max_value)) for _ in range(n)]
        category1.append((n, G, items))

        # Generate Category 2 (varying G, fixed n)
        n = max_items  # Fixed number of items for this category
        G = random.randint(1, max_capacity)
        items = [(random.randint(1, max_weight), random.randint(1, max_value)) for _ in range(n)]
        category2.append((n, G, items))

    return category1, category2

def save_test_cases_to_files(test_cases, output_dir="tests"):
    """
    Save generated test cases to text files.

    :param test_cases: List of test cases generated by `generate_knapsack_tests`
    :param output_dir: Directory to save the test files
    """
    import os

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    for i, (n, G, items) in enumerate(test_cases):
        filename = os.path.join(output_dir, f"test_case_{i + 1}.txt")
        with open(filename, "w") as f:
            f.write(f"{n} {G}\n")
            for weight, value in items:
                f.write(f"{weight} {value}\n")

if __name__ == "__main__":
    # Parameters for test generation
    num_tests = 20        # Number of test cases to generate
    max_items = 50       # Maximum number of items per test case
    max_capacity = 25     # Maximum capacity of the knapsack
    max_weight = 15       # Maximum weight of an item
    max_value = 30       # Maximum value of an item

    # Generate test cases
    category1, category2 = generate_knapsack_tests(num_tests, max_items, max_capacity, max_weight, max_value)

    # Save test cases to files
    save_test_cases_to_files(category1, output_dir="tests/category1")
    save_test_cases_to_files(category2, output_dir="tests/category2")

    print(f"Generated {num_tests} test cases for Category 1 and Category 2.")
