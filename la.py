class TreeHouse:
    def __init__(self, house_id):
        self.house_id = house_id
        self.energy = 0
        self.children = []

class BytepixieEnergyTracker:
    def __init__(self):
        self.treehouses = {}

    def build_network(self, connections):
        for parent, child in connections:
            if parent not in self.treehouses:
                self.treehouses[parent] = TreeHouse(parent)
            if child not in self.treehouses:
                self.treehouses[child] = TreeHouse(child)
            self.treehouses[parent].children.append(self.treehouses[child])

    def update_energy(self, house_id, energy):
        if house_id in self.treehouses:
            self.treehouses[house_id].energy = energy

    def total_subtree_energy(self, house_id):
        def dfs(node):
            total = node.energy
            for child in node.children:
                total += dfs(child)
            return total

        if house_id in self.treehouses:
            return dfs(self.treehouses[house_id])
        return 0

    def min_energy_in_subtree(self, house_id):
        def dfs(node):
            min_energy = node.energy
            for child in node.children:
                min_energy = min(min_energy, dfs(child))
            return min_energy

        if house_id in self.treehouses:
            return dfs(self.treehouses[house_id])
        return float('inf')

    def shadowbug_detected(self, house_id):
        def dfs(node):
            if node.energy < 0:
                return True
            return any(dfs(child) for child in node.children)

        if house_id in self.treehouses:
            return dfs(self.treehouses[house_id])
        return False

def process_queries(connections, queries):
    tracker = BytepixieEnergyTracker()
    tracker.build_network(connections)
    results = []

    for query in queries:
        operation = query[0]
        if operation == "UPDATE":
            tracker.update_energy(query[1], query[2])
            results.append(None)
        elif operation == "TOTAL":
            results.append(tracker.total_subtree_energy(query[1]))
        elif operation == "MIN":
            results.append(tracker.min_energy_in_subtree(query[1]))
        elif operation == "SHADOWBUG":
            results.append(tracker.shadowbug_detected(query[1]))

    return results

# Test cases
def run_test_cases():
    test_cases = [
        # Test case 1: Normal case
        {
            "connections": [(1, 2), (1, 3), (2, 4), (2, 5)],
            "queries": [
                ("UPDATE", 1, 5),
                ("UPDATE", 2, 3),
                ("UPDATE", 3, 7),
                ("UPDATE", 4, 2),
                ("UPDATE", 5, 1),
                ("TOTAL", 1),
                ("MIN", 1),
                ("SHADOWBUG", 1)
            ],
            "expected": [None, None, None, None, None, 18, 1, False]
        },
        # Test case 2: Normal case with negative energy
        {
            "connections": [(1, 2), (1, 3), (2, 4)],
            "queries": [
                ("UPDATE", 1, 10),
                ("UPDATE", 2, -5),
                ("UPDATE", 3, 7),
                ("UPDATE", 4, 3),
                ("TOTAL", 1),
                ("MIN", 1),
                ("SHADOWBUG", 1)
            ],
            "expected": [None, None, None, None, 15, -5, True]
        },
        # Test case 3: Normal case with single node
        {
            "connections": [],
            "queries": [
                ("UPDATE", 1, 100),
                ("TOTAL", 1),
                ("MIN", 1),
                ("SHADOWBUG", 1)
            ],
            "expected": [None, 100, 100, False]
        },
        # Test case 4: Normal case with multiple updates
        {
            "connections": [(1, 2), (1, 3)],
            "queries": [
                ("UPDATE", 1, 5),
                ("UPDATE", 2, 3),
                ("UPDATE", 3, 7),
                ("TOTAL", 1),
                ("UPDATE", 2, 10),
                ("TOTAL", 1),
                ("MIN", 1)
            ],
            "expected": [None, None, None, 15, None, 22, 5]
        },
        # Test case 5: Edge case - Query non-existent node
        {
            "connections": [(1, 2), (1, 3)],
            "queries": [
                ("UPDATE", 1, 5),
                ("UPDATE", 2, 3),
                ("TOTAL", 4),
                ("MIN", 4),
                ("SHADOWBUG", 4)
            ],
            "expected": [None, None, 0, float('inf'), False]
        },
        # Test case 6: Edge case - Empty tree
        {
            "connections": [],
            "queries": [
                ("TOTAL", 1),
                ("MIN", 1),
                ("SHADOWBUG", 1)
            ],
            "expected": [0, float('inf'), False]
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        connections = test_case["connections"]
        queries = test_case["queries"]
        expected = test_case["expected"]
        result = process_queries(connections, queries)
        
        print(f"Test case {i}:")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print("Passed" if result == expected else "Failed")
        print()

# Run the test cases
run_test_cases()
