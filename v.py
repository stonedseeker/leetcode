from collections import defaultdict

def count_harmonious_paths(melody_graph: dict[str, dict[str, int]]) -> int:
    if not melody_graph:
        return 0

    # Validate input
    valid_notes = set('ABCDEFG')
    for note, transitions in melody_graph.items():
        if not isinstance(note, str) or note not in valid_notes:
            raise ValueError("Musical notes must be represented by letters A through G")
        for next_note, weight in transitions.items():
            if not isinstance(next_note, str) or next_note not in valid_notes:
                raise ValueError("Musical notes must be represented by letters A through G")
            if not isinstance(weight, int) or weight < 1 or weight > 10:
                raise ValueError("Emotional impact (edge weights) must be between 1 and 10")

    def dfs(note, path, total_weight):
        if len(path) >= 4 and total_weight % 7 == 0:
            nonlocal count
            count += 1

        for next_note, weight in melody_graph[note].items():
            if next_note not in path or (len(path) >= 3 and next_note == path[0]):
                dfs(next_note, path + [next_note], total_weight + weight)

    count = 0
    for start_note in melody_graph:
        dfs(start_note, [start_note], 0)

    return count

# 
# Test case 1: Simple melody graph
# Test case 1: Melody graph with harmonious paths
melody1 = {
    'A': {'B': 3, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'D': 1, 'F': 6},
    'D': {'G': 3},
    'E': {'G': 4},
    'F': {'G': 2},
    'G': {'A': 1}
}
print("TC1: Expected: 3")
print("TC1: True:", count_harmonious_paths(melody1))

# Test case 2: Melody graph with no harmonious paths
melody2 = {
    'A': {'B': 1, 'C': 2},
    'B': {'C': 3},
    'C': {'A': 4}
}
print("TC2: Expected: 0")
print("TC2: True:", count_harmonious_paths(melody2))

# Test case 3: Melody graph with multiple harmonious paths
melody3 = {
    'A': {'B': 2, 'C': 3, 'D': 4},
    'B': {'C': 5, 'D': 6, 'E': 7},
    'C': {'D': 1, 'E': 2, 'F': 3},
    'D': {'E': 4, 'F': 5, 'G': 6},
    'E': {'F': 7, 'G': 1},
    'F': {'G': 2},
    'G': {'A': 3}
}
print("TC3: Expected: 12")
print("TC3: True:", count_harmonious_paths(melody3))

# Test case 4: Melody graph with only one note
melody4 = {'A': {}}
print("TC4: Expected: 0")
print("TC4: True:", count_harmonious_paths(melody4))

# Test case 5: Melody graph with disconnected components
melody5 = {
    'A': {'B': 1},
    'B': {'C': 2},
    'C': {'A': 4},
    'D': {'E': 3},
    'E': {'F': 5},
    'F': {'G': 6},
    'G': {'D': 7}
}
print("TC5: Expected: 2")
print("TC5: True:", count_harmonious_paths(melody5))

# Test case 6: Empty melody graph
melody6 = {}
print("TC6: Expected: 0")
print("TC6: True:", count_harmonious_paths(melody6))

# Test case 7: Invalid input - non-string keys
try:
    count_harmonious_paths({1: {2: 3}})
    print("TC7: Expected ValueError, got no error")
except ValueError as e:
    print("TC7: Expected: 'Musical notes must be represented by letters A through G'")
    print("TC7: True:", e)

# Test case 8: Invalid input - negative edge weights
try:
    count_harmonious_paths({'A': {'B': -1}})
    print("TC8: Expected ValueError, got no error")
except ValueError as e:
    print("TC8: Expected: 'Emotional impact (edge weights) must be between 1 and 10'")
    print("TC8: True:", e)

# Test case 9: Invalid input - edge weights out of range
try:
    count_harmonious_paths({'A': {'B': 11}})
    print("TC9: Expected ValueError, got no error")
except ValueError as e:
    print("TC9: Expected: 'Emotional impact (edge weights) must be between 1 and 10'")
    print("TC9: True:", e)
