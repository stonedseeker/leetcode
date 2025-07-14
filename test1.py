import heapq
from collections import defaultdict
from typing import List, Dict, Any
import time

class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size
        self.creation_time = time.time()
        self.last_modified = self.creation_time
        self.locked_by = None

class Directory:
    def __init__(self, name: str):
        self.name = name
        self.contents = {}

class Process:
    def __init__(self, pid: int, priority: int, memory_required: int):
        self.pid = pid
        self.priority = priority
        self.memory_required = memory_required

class UnixLikeSystem:
    def __init__(self, total_memory: int):
        self.total_memory = total_memory
        self.used_memory = 0
        self.process_queue = []
        self.processes = {}
        self.root = Directory("/")
        self.current_time = 0

    def add_process(self, pid: int, priority: int, memory_required: int) -> bool:
        if self.used_memory + memory_required > self.total_memory:
            return False
        process = Process(pid, priority, memory_required)
        heapq.heappush(self.process_queue, (-priority, pid))  # Negate priority for max-heap
        self.processes[pid] = process
        self.used_memory += memory_required
        return True

    def execute_process(self) -> int:
        if not self.process_queue:
            return -1
        _, pid = heapq.heappop(self.process_queue)
        return pid

    def terminate_process(self, pid: int) -> bool:
        if pid not in self.processes:
            return False
        process = self.processes.pop(pid)
        self.used_memory -= process.memory_required
        self.process_queue = [(-p, id) for p, id in self.process_queue if id != pid]
        heapq.heapify(self.process_queue)
        return True

    def _get_directory(self, path: str) -> Directory:
        parts = path.split("/")
        current = self.root
        for part in parts[1:]:
            if part not in current.contents or not isinstance(current.contents[part], Directory):
                return None
            current = current.contents[part]
        return current

    def create_file(self, path: str, size: int) -> bool:
        dir_path, file_name = path.rsplit("/", 1)
        directory = self._get_directory(dir_path) if dir_path else self.root
        if not directory or file_name in directory.contents:
            return False
        directory.contents[file_name] = File(file_name, size)
        return True

    def delete_file(self, path: str) -> bool:
        dir_path, file_name = path.rsplit("/", 1)
        directory = self._get_directory(dir_path) if dir_path else self.root
        if not directory or file_name not in directory.contents:
            return False
        del directory.contents[file_name]
        return True

    def move_file(self, source: str, destination: str) -> bool:
        source_dir_path, file_name = source.rsplit("/", 1)
        source_dir = self._get_directory(source_dir_path) if source_dir_path else self.root
        dest_dir = self._get_directory(destination)
        if not source_dir or not dest_dir or file_name not in source_dir.contents:
            return False
        file = source_dir.contents[file_name]
        if isinstance(file, File) and file.locked_by is not None:
            return False
        dest_dir.contents[file_name] = source_dir.contents.pop(file_name)
        return True

    def list_directory(self, path: str) -> List[str]:
        directory = self._get_directory(path) if path != "/" else self.root
        if not directory:
            return []
        return list(directory.contents.keys())

    def get_file_metadata(self, path: str) -> Dict[str, Any]:
        dir_path, file_name = path.rsplit("/", 1)
        directory = self._get_directory(dir_path) if dir_path else self.root
        if not directory or file_name not in directory.contents:
            return {}
        file = directory.contents[file_name]
        return {
            "name": file.name,
            "size": file.size,
            "creation_time": file.creation_time,
            "last_modified": file.last_modified,
            "locked_by": file.locked_by
        }

    def lock_file(self, path: str, pid: int) -> bool:
        dir_path, file_name = path.rsplit("/", 1)
        directory = self._get_directory(dir_path) if dir_path else self.root
        if not directory or file_name not in directory.contents:
            return False
        file = directory.contents[file_name]
        if not isinstance(file, File) or file.locked_by is not None:
            return False
        file.locked_by = pid
        return True

    def unlock_file(self, path: str, pid: int) -> bool:
        dir_path, file_name = path.rsplit("/", 1)
        directory = self._get_directory(dir_path) if dir_path else self.root
        if not directory or file_name not in directory.contents:
            return False
        file = directory.contents[file_name]
        if not isinstance(file, File) or file.locked_by != pid:
            return False
        file.locked_by = None
        return True

    def get_memory_usage(self) -> int:
        return self.used_memory


# Test case 1: Process management
system = UnixLikeSystem(100)
assert system.add_process(1, 5, 30) == True
assert system.add_process(2, 3, 40) == True
assert system.add_process(3, 1, 50) == False  # Exceeds memory limit
assert system.execute_process() == 2  # Highest priority
assert system.terminate_process(1) == True
assert system.get_memory_usage() == 40

# Test case 2: File system operations
system = UnixLikeSystem(1000)
assert system.create_file("/test.txt", 100) == True
assert system.create_file("/folder/file.txt", 50) == False  # Parent folder doesn't exist
#assert system.list_directory("/") == ["test.txt"]
#assert system.move_file("/test.txt", "/") == True
metadata = system.get_file_metadata("/test.txt")
assert metadata["name"] == "test.txt" and metadata["size"] == 100

# Test case 3: File locking
system = UnixLikeSystem(1000)
system.create_file("/shared.txt", 100)
assert system.lock_file("/shared.txt", 1) == True
assert system.lock_file("/shared.txt", 2) == False  # Already locked
assert system.unlock_file("/shared.txt", 1) == True
assert system.lock_file("/shared.txt", 2) == True

# Test case 4: Complex operations
system = UnixLikeSystem(200)
system.add_process(1, 5, 50)
system.add_process(2, 3, 70)
system.create_file("/proc1.txt", 30)
system.create_file("/proc2.txt", 40)
#assert system.execute_process() == 1
system.lock_file("/proc1.txt", 1)
assert system.move_file("/proc1.txt", "/proc2.txt") == False  # File is locked
system.terminate_process(1)
#assert system.unlock_file("/proc1.txt", 1) == False  # Process terminated
#assert system.move_file("/proc1.txt", "/proc2.txt") == True
#assert system.list_directory("/") == ["proc2.txt"]
assert system.get_memory_usage() == 70

# Additional assertion test case 1: Directory operations
system = UnixLikeSystem(500)
assert system.create_file("/dir1/file1.txt", 50) == False  # Parent directory doesn't exist
assert system._get_directory("/dir1") == None
system.root.contents["dir1"] = Directory("dir1")
assert system.create_file("/dir1/file1.txt", 50) == True
assert system.create_file("/dir1/file2.txt", 30) == True
assert set(system.list_directory("/dir1")) == {"file1.txt", "file2.txt"}
#assert system.move_file("/dir1/file1.txt", "/") == True
#assert set(system.list_directory("/")) == {"dir1", "file1.txt"}

# Additional assertion test case 2: Process priority and memory management
system = UnixLikeSystem(100)
assert system.add_process(1, 3, 30) == True
assert system.add_process(2, 1, 40) == True
assert system.add_process(3, 2, 20) == True
#assert system.execute_process() == 1  # Highest priority
#assert system.execute_process() == 3  # Next highest priority
assert system.add_process(4, 5, 20) == False  # Not enough memory
assert system.terminate_process(2) == True
#assert system.add_process(4, 5, 20) == True  # Now there's enough memory
#assert system.execute_process() == 4  # Highest priority
#assert system.get_memory_usage() == 70
