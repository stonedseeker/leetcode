from collections import defaultdict

def count_efficient_cascades(reaction_graph: dict[str, dict[str, int]]) -> int:
    if not reaction_graph:
        return 0

    # Validate input
    for compound, reactions in reaction_graph.items():
        if not isinstance(compound, str):
            raise ValueError("Compound identifiers must be strings")
        if compound in reactions:
            raise ValueError("Self-loops are not allowed in the reaction graph")
        for product, energy in reactions.items():
            if not isinstance(product, str):
                raise ValueError("Compound identifiers must be strings")
            if not isinstance(energy, int) or energy <= 0:
                raise ValueError("Energy costs must be positive integers")

    def dfs(compound, path, total_energy):
        if len(path) >= 4 and total_energy % 5 == 0:
            if len(path) == 4 or path[-1] != path[0]:
                nonlocal count
                count += 1
            elif len(path) > 4:
                count += 1

        for product, energy in reaction_graph[compound].items():
            if product not in path or (len(path) > 3 and product == path[0]):
                dfs(product, path + [product], total_energy + energy)

    count = 0
    for start_compound in reaction_graph:
        dfs(start_compound, [start_compound], 0)

    return count

# Test cases
def test_count_efficient_cascades():
    reactions1 = {
        'A': {'B': 2, 'C': 3},
        'B': {'D': 4, 'E': 1},
        'C': {'D': 2, 'F': 3},
        'D': {'G': 5},
        'E': {'G': 4},
        'F': {'G': 1},
        'G': {'A': 5}
    }
    print("Test Case 1:")
    print(f"Expected Count: 3")
    print(f"Observed Count: {count_efficient_cascades(reactions1)}\n") 

    # ... (Similarly structure the rest of your test cases)

    # Test case 2: Reaction graph with no efficient cascades
    reactions2 = {
        'A': {'B': 1, 'C': 2},
        'B': {'C': 3},
        'C': {'A': 4}
    }
    print("Test Case 2:")
    print("Expected Count: 0")
    print(f"Observed Count: {count_efficient_cascades(reactions2)}\n")

    # Test case 3: Reaction graph with multiple efficient cascades
    reactions3 = {
        'A': {'B': 2, 'C': 3, 'D': 4},
        'B': {'C': 5, 'D': 6, 'E': 7},
        'C': {'D': 1, 'E': 2, 'F': 3},
        'D': {'E': 4, 'F': 5, 'G': 6},
        'E': {'F': 7, 'G': 1},
        'F': {'G': 2},
        'G': {'A': 3}
    }
    print("Test Case 3:")
    print("Expected Count: 12")
    print(f"Observed Count: {count_efficient_cascades(reactions3)}\n") 

    # Test case 4: Reaction graph with only one compound
    reactions4 = {'A': {}}
    print("Test Case 4:")
    print("Expected Count: 0")
    print(f"Observed Count: {count_efficient_cascades(reactions4)}\n") 

    # Test case 5: Reaction graph with disconnected components
    reactions5 = {
        'A': {'B': 1},
        'B': {'C': 2},
        'C': {'A': 4},
        'D': {'E': 3},
        'E': {'F': 5},
        'F': {'G': 6},
        'G': {'D': 7}
    }
    print("Test Case 5:")
    print("Expected Count: 2")
    print(f"Observed Count: {count_efficient_cascades(reactions5)}\n") 

    # Test case 6: Empty reaction graph
    reactions6 = {}
    print("Test Case 6:")
    print("Expected Count: 0")
    print(f"Observed Count: {count_efficient_cascades(reactions6)}\n")
    # Test case 7: Invalid input - non-string keys
    reactions7 = {1: {2: 3}}
    print("Test Case 7: (Invalid Input)")
    print(f"Reactions: {reactions7}")
    print(f"Expected Exception: ValueError: Compound identifiers must be strings\n")

    # Test case 8: Invalid input - negative energy costs
    reactions8 = {'A': {'B': -1}}
    print("Test Case 8: (Invalid Input)")
    print(f"Reactions: {reactions8}")
    print(f"Expected Exception: ValueError: Energy costs must be positive integers\n")

    # Test case 9: Invalid input - non-integer energy costs
    reactions9 = {'A': {'B': 1.5}}
    print("Test Case 9: (Invalid Input)")
    print(f"Reactions: {reactions9}")
    print(f"Expected Exception: ValueError: Energy costs must be positive integers\n")

    # Test case 10: Invalid input - self-loops
    reactions10 = {'A': {'A': 5}}
    print("Test Case 10: (Invalid Input)")
    print(f"Reactions: {reactions10}")
    print(f"Expected Exception: ValueError: Self-loops are not allowed in the reaction graph\n")

# Run the tests
test_count_efficient_cascades()
