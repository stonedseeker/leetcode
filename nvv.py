from typing import List, Tuple

def find_minimum_captures(n: int, roads: List[Tuple[int, int]], plans: List[List[int]]) -> List[int]:
    adj = [[] for _ in range(n + 1)]
    for u, v in roads:
        adj[u].append(v)
        adj[v].append(u)

    results = []
    for plan in plans:
        k = plan[0]
        important_towns = plan[1:]

        if k <= 1:
            results.append(-1)
            continue

        min_captures = float('inf')

        for i in range(1 << n):  # Iterate through all subsets of towns
            captures = []
            for j in range(n):
                if (i >> j) & 1:
                    captures.append(j + 1)

            is_isolated = True
            for t1 in range(len(important_towns)):
                for t2 in range(t1 + 1, len(important_towns)):
                    q = [(important_towns[t1], [important_towns[t1]])]
                    reachable = False
                    while q:
                        curr, path = q.pop(0)
                        if curr == important_towns[t2]:
                            reachable = True
                            break
                        for neighbor in adj[curr]:
                            if neighbor not in path and neighbor not in captures:
                                q.append((neighbor, path + [neighbor]))
                    if reachable:
                        is_isolated = False
                        break
                if not is_isolated:
                    break

            if is_isolated:
                min_captures = min(min_captures, len(captures))

        results.append(min_captures if min_captures != float('inf') else -1)

    return results


# Test Cases
n = 4
roads = [(1, 3), (2, 3), (4, 3)]
plans = [[2, 1, 2], [3, 2, 3, 4], [3, 1, 2, 4], [4, 1, 2, 3, 4]]
expected_output = [1, -1, 1, -1]
obtained_output = find_minimum_captures(n, roads, plans)
print(f"Test Case 1: Expected = {expected_output}, Obtained = {obtained_output}")


n = 7
roads = [(1, 2), (2, 3), (3, 4), (1, 5), (5, 6), (5, 7)]
plans = [[4, 2, 4, 6, 7]]
expected_output = [2]
obtained_output = find_minimum_captures(n, roads, plans)
print(f"Test Case 2: Expected = {expected_output}, Obtained = {obtained_output}")



n = 7
roads = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7)]
plans = [[4, 1, 3, 5, 7], [3, 2, 4, 6], [2, 1, 7], [2, 3, 4], [3, 1, 6, 7]]
expected_output = [3, 2, 1, -1, -1]
obtained_output = find_minimum_captures(n, roads, plans)
print(f"Test Case 3: Expected = {expected_output}, Obtained = {obtained_output}")



n = 30
roads = [(1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (2, 7), (4, 8), (4, 9), (6, 10), (6, 11), (11, 30), (11, 23), (30, 24), (30, 25), (25, 26), (25, 27), (27, 29), (27, 28), (23, 20), (23, 22), (20, 21), (20, 19), (3, 12), (3, 13), (13, 14), (13, 15), (15, 16), (15, 17), (15, 18)]
plans = [[6, 17, 25, 20, 5, 9, 13], [10, 2, 4, 3, 14, 16, 18, 22, 29, 30, 19]]
expected_output = [3, 6]
obtained_output = find_minimum_captures(n, roads, plans)
print(f"Test Case 4: Expected = {expected_output}, Obtained = {obtained_output}")
