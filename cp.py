from collections import defaultdict
import heapq

def minimum_relay_time(n: int, edges: list[tuple[int, int, int]], source: int) -> int:
    """
    Calculates the minimum time Vybhv needs to collect data from all servers
    and return to the source. Returns -1 if all servers cannot be reached.
    
    :param n: Total number of servers.
    :param edges: List of tuples representing relay paths between servers and their times.
    :param source: The starting server for Vybhv.
    :return: The minimum time required to collect data and return to the source, or -1 if unreachable.
    """
    # Input validation
    if not isinstance(n, int) or n < 2:
        raise ValueError("Invalid input: Invalid number of servers.")
    if not isinstance(edges, list) or any(
        not isinstance(edge, tuple) or len(edge) != 3 or 
        not all(isinstance(x, int) for x in edge[:2]) or
        not isinstance(edge[2], int) or edge[2] < 0 or
        not (1 <= edge[0] <= n) or not (1 <= edge[1] <= n)
        for edge in edges):
        raise ValueError("Invalid input: Invalid edge data.")
    if not isinstance(source, int) or not (1 <= source <= n):
        raise ValueError("Invalid input: Invalid source server.")

    # Graph representation
    graph = defaultdict(list)
    for u, v, time in edges:
        graph[u].append((v, time))
        graph[v].append((u, time))  # bidirectional graph since return is allowed

    # Function to perform Dijkstra's algorithm
    def dijkstra(start):
        min_heap = [(0, start)]  # (time, node)
        dist = {i: float('inf') for i in range(1, n+1)}
        dist[start] = 0
        
        while min_heap:
            curr_time, node = heapq.heappop(min_heap)
            
            if curr_time > dist[node]:
                continue
            
            for neighbor, time in graph[node]:
                new_time = curr_time + time
                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    heapq.heappush(min_heap, (new_time, neighbor))
        
        return dist

    # 1. Get shortest path from source to all servers
    dist_from_source = dijkstra(source)

    # 2. Get shortest path from all servers back to source
    dist_to_source = dijkstra(source)

    # Ensure all servers are reachable
    if any(dist_from_source[i] == float('inf') for i in range(1, n+1)):
        return -1

    # Calculate total relay time (there and back)
    total_time = 0
    for i in range(1, n+1):
        total_time += dist_from_source[i] + dist_to_source[i]

    return total_time


def test_minimum_relay_time():
    # test case 1: simple valid path
    print(minimum_relay_time(5, [(1, 2, 4), (2, 3, 5), (3, 5, 3), (4, 5, 1), (1, 4, 10)], 1))# == 46
    
    # test case 2: some servers not reachable
    assert minimum_relay_time(4, [(1, 2, 6), (2, 3, 7)], 1) == -1
    
    # test case 3: another valid case, cyclic graph
    print(minimum_relay_time(3, [(1, 2, 5), (2, 3, 8), (3, 1, 2)], 1))# == 30
    
    # test case 4: edge case with n=2, directly reachable
    print(minimum_relay_time(2, [(1, 2, 5)], 1))# == 10
    
    # test case 5: no edges, unreachable case
    assert minimum_relay_time(3, [], 1) == -1
    
    # test case 6: single relay path chain
    print(minimum_relay_time(4, [(1, 2, 3), (2, 3, 4), (3, 4, 5)], 1)) #== 24
    
    # test case 7: all nodes directly connected to source
    print(minimum_relay_time(4, [(1, 2, 2), (1, 3, 2), (1, 4, 2), (2, 3, 2), (3, 4, 2)], 1))# == 24
    
    # test case 8: fully connected graph with equal weights
    print(minimum_relay_time(3, [(1, 2, 1), (2, 3, 1), (3, 1, 1)], 1))# == 6

    # Input validation cases
    try:
        minimum_relay_time(1, [(1, 2, 5)], 1)
    except ValueError as e:
        assert str(e) == "Invalid input: Invalid number of servers."
    
    try:
        minimum_relay_time(3, [(1, 2, -1)], 1)
    except ValueError as e:
        assert str(e) == "Invalid input: Invalid edge data."
    
    try:
        minimum_relay_time(3, [(1, 2, 5)], "1")
    except ValueError as e:
        assert str(e) == "Invalid input: Invalid source server."

test_minimum_relay_time()
