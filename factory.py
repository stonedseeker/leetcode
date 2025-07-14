from collections import deque
from queue import PriorityQueue
from typing import List

class DoublyLinkedListNode:
    def __init__(self, recycle_code):
        self.recycle_code = recycle_code
        self.prev = None
        self.next = None

class RecyclingFacility:
    def __init__(self):
        self.conveyor_belt = deque()
        self.sorting_bins = {"processor": [], "memory": [], "battery": []}
        self.priority_queue = PriorityQueue()
        self.sorted_list_head = None
        self.sorted_list_tail = None

    def add_component(self, type: str, value: int, recycle_code: str) -> None:
        if type not in self.sorting_bins:
            raise ValueError("Invalid component type")
        if not 1 <= value <= 100:
            raise ValueError("Value must be between 1 and 100")
        if not recycle_code:
            raise ValueError("Recycle code cannot be empty")

        self.conveyor_belt.append((type, value, recycle_code))

    def _add_to_sorted_list(self, recycle_code):
        new_node = DoublyLinkedListNode(recycle_code)
        if not self.sorted_list_head:
            self.sorted_list_head = self.sorted_list_tail = new_node
        else:
            self.sorted_list_tail.next = new_node
            new_node.prev = self.sorted_list_tail
            self.sorted_list_tail = new_node

    def _process_bin(self, bin_type):
        while len(self.sorting_bins[bin_type]) >= 5:
            for _ in range(5):
                self._add_to_sorted_list(self.sorting_bins[bin_type].pop()[2])

    def _process_priority_queue(self):
        while self.priority_queue.qsize() >= 3:
            for _ in range(3):
                _, _, recycle_code = self.priority_queue.get()
                self._add_to_sorted_list(recycle_code)

    def process_components(self) -> List[str]:
        while self.conveyor_belt:
            type, value, recycle_code = self.conveyor_belt.popleft()
            if value >= 75:
                self.priority_queue.put((-value, type, recycle_code))
            else:
                self.sorting_bins[type].append((value, type, recycle_code))

            self._process_bin(type)
            self._process_priority_queue()

        # Process remaining components
        for bin_type in self.sorting_bins:
            while self.sorting_bins[bin_type]:
                self._add_to_sorted_list(self.sorting_bins[bin_type].pop()[2])

        while not self.priority_queue.empty():
            _, _, recycle_code = self.priority_queue.get()
            self._add_to_sorted_list(recycle_code)

        # Collect final sorted order
        result = []
        current = self.sorted_list_head
        while current:
            result.append(current.recycle_code)
            current = current.next

        return result

# Test cases
print("Test case 1: Normal operation")
facility = RecyclingFacility()
components = [
    ("processor", 50, "P001"),
    ("memory", 80, "M001"),
    ("battery", 30, "B001"),
    ("processor", 90, "P002"),
    ("memory", 60, "M002"),
    ("battery", 70, "B002"),
    ("processor", 40, "P003"),
    ("memory", 85, "M003"),
    ("battery", 55, "B003"),
]
for comp in components:
    facility.add_component(*comp)
result = facility.process_components()
print(f"Expected: ['P001', 'B001', 'M002', 'B002', 'P003', 'B003', 'M001', 'P002', 'M003']")
print(f"Got:      {result}")

print("\nTest case 2: Empty input")
facility = RecyclingFacility()
result = facility.process_components()
print(f"Expected: []")
print(f"Got:      {result}")

print("\nTest case 3: All high-value components")
facility = RecyclingFacility()
for i in range(1, 6):
    facility.add_component("processor", 80, f"P00{i}")
result = facility.process_components()
print(f"Expected: ['P001', 'P002', 'P003', 'P004', 'P005']")
print(f"Got:      {result}")

print("\nTest case 4: All low-value components")
facility = RecyclingFacility()
for i in range(1, 6):
    facility.add_component("memory", 50, f"M00{i}")
result = facility.process_components()
print(f"Expected: ['M001', 'M002', 'M003', 'M004', 'M005']")
print(f"Got:      {result}")

print("\nTest case 5: Mixed high and low-value components")
facility = RecyclingFacility()
components = [("processor", 60, "P001"), ("memory", 80, "M001"), ("battery", 90, "B001"),
              ("processor", 75, "P002"), ("memory", 40, "M002"), ("battery", 30, "B002")]
for comp in components:
    facility.add_component(*comp)
result = facility.process_components()
print(f"Expected: ['P001', 'M002', 'B002', 'M001', 'B001', 'P002']")
print(f"Got:      {result}")

print("\nTest case 6: Invalid component type")
facility = RecyclingFacility()
try:
    facility.add_component("gpu", 50, "G001")
    print("Failed: Should raise ValueError")
except ValueError as e:
    print(f"Caught ValueError: {str(e)}")

print("\nTest case 7: Invalid value (too low)")
facility = RecyclingFacility()
try:
    facility.add_component("processor", 0, "P001")
    print("Failed: Should raise ValueError")
except ValueError as e:
    print(f"Caught ValueError: {str(e)}")

print("\nTest case 8: Invalid value (too high)")
facility = RecyclingFacility()
try:
    facility.add_component("memory", 101, "M001")
    print("Failed: Should raise ValueError")
except ValueError as e:
    print(f"Caught ValueError: {str(e)}")

print("\nTest case 9: Empty recycle code")
facility = RecyclingFacility()
try:
    facility.add_component("battery", 50, "")
    print("Failed: Should raise ValueError")
except ValueError as e:
    print(f"Caught ValueError: {str(e)}")

print("\nTest case 10: Large input")
facility = RecyclingFacility()
for i in range(1000):
    facility.add_component("processor", i % 100 + 1, f"P{i:03d}")
result = facility.process_components()
print(f"Expected length: 1000")
print(f"Got length:      {len(result)}")
print(f"First 10 items:  {result[:10]}")
print(f"Last 10 items:   {result[-10:]}")
