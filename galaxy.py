class StarSystem:
    def __init__(self, system_id: int, resources: list[int]):
        self.system_id = system_id
        self.resources = resources
        self.hash_link = None
        self.next = None 


def create_galaxy(system_data: list[tuple[int, list[int]]]) -> 'StarSystem':
    """Creates a linked list representation of a galaxy based on the given star system data.
    Returns the head of the linked list."""
    galaxy = []
    for system_id, resources in system_data:
        galaxy.append(StarSystem(system_id, resources))

    n = len(galaxy)
    head = galaxy[0] if galaxy else None
    current = head
    for i in range(1, n):
        current.next = galaxy[i] 
        current = current.next

    for i, system in enumerate(galaxy):
        hash_value = sum(system.resources) % n
        if hash_value < n:
            system.hash_link = galaxy[hash_value]
    return head 


def find_trade_route(head: 'StarSystem', resource_a: int, resource_b: int) -> list[int] | None:
    """Finds the shortest trade route between two star systems containing the specified resources 
    within a linked list representation of a galaxy. 
    Returns a list of system IDs representing the route, or None if no route is found."""
    if not head:
        return None

    visited = set()
    queue = [(head, [head.system_id])]  # Use a queue for BFS

    while queue:
        current, path = queue.pop(0)
        print(f"Current system: {current.system_id}, Path: {path}") # for debugging

        if resource_a in current.resources and resource_b in current.resources:
            return path

        visited.add(current)

        for neighbor in [current.hash_link, current.next]:
            if neighbor and neighbor not in visited:
                queue.append((neighbor, path + [neighbor.system_id]))

    return None 
  
"""This code defines a system for finding trade routes between star systems in a galaxy.
It uses a linked list representation, with a hashing function to link systems with shared resources.
It includes functions to create the galaxy and find the shortest trade route between two resources."""


# Test Cases:

## --- Focusing on `create_galaxy` and basic traversal ---

# Test Case 1: Simple Linear Galaxy 
system_data = [(1, [1, 2]), (2, [3, 4])]
galaxy_head = create_galaxy(system_data)
assert galaxy_head.system_id == 1, "Testcase 1a failed: Head incorrect."
assert galaxy_head.next.system_id == 2, "Testcase 1b failed: Linear connection failed"

# Test Case 2: Galaxy with Hash Links
system_data = [(1, [1, 2, 3]), (2, [4, 5]), (3, [2, 5]), (4, [1, 4])]
galaxy_head = create_galaxy(system_data)
assert galaxy_head.hash_link.system_id == 4, "Testcase 2a failed: Hash link calculation incorrect."
assert galaxy_head.next.hash_link.system_id == 3, "Testcase 2b failed: Hash link calculation incorrect."

## --- Basic `find_trade_route` tests ---

# Test Case 3: Resources in the Same System
system_data = [(1, [1, 2, 3]), (2, [4, 5])]
galaxy_head = create_galaxy(system_data)
trade_route = find_trade_route(galaxy_head, 1, 3) 
assert trade_route == [1], "Testcase 3 failed: Should find resources in the same system."

# Test Case 4: Direct Linear Path
system_data = [(1, [1, 2]), (2, [2, 3])]
galaxy_head = create_galaxy(system_data)
trade_route = find_trade_route(galaxy_head, 1, 3)
assert trade_route == [1, 2], "Testcase 4 failed: Should find a direct linear path."

print("Basic tests completed. Still debugging `find_trade_route` for shortest path logic.") 
