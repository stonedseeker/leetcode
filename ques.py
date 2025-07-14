from collections import defaultdict

def resolve_command_order(commands):
   # Create a graph representation of the dependencies
   graph = defaultdict(list)
   in_degrees = {cmd: 0 for cmd, _, _ in commands}

   for cmd, _, deps in commands:
       for dep in deps:
           graph[dep].append(cmd)
           in_degrees[cmd] += 1

   # Topological sort to find the order of execution
   order = []
   queue = [cmd for cmd, degree in in_degrees.items() if degree == 0]

   while queue:
       curr = queue.pop(0)
       order.append(curr)

       for neighbor in graph[curr]:
           in_degrees[neighbor] -= 1
           if in_degrees[neighbor] == 0:
               queue.append(neighbor)

   # Check if there is a cyclic dependency
   if any(degree > 0 for degree in in_degrees.values()):
       return "Dependency resolution failed"

   # Convert the order to the desired output format
   result = []
   for cmd in order:
       for command in commands:
           if command[0] == cmd:
               result.append(command)

   return result


def test_resolve_command_order():
   # Test case 1: Simple case
   commands = [
       ("VM1", "command1", []),
       ("VM2", "command2", []),
       ("VM3", "command3", ["command1", "command2"])
   ]
   expected_output = [
       ("VM1", "command1", []),
       ("VM2", "command2", []),
       ("VM3", "command3", ["command1", "command2"])
   ]
   assert resolve_command_order(commands) == expected_output

   # Test case 2: Cyclic dependency
   commands = [
       ("VM1", "command1", ["command2"]),
       ("VM2", "command2", ["command3"]),
       ("VM3", "command3", ["command1"])
   ]
   assert resolve_command_order(commands) == "Dependency resolution failed"

   # Test case 3: Multiple dependencies
   commands = [
       ("VM1", "command1", []),
       ("VM2", "command2", ["command1"]),
       ("VM3", "command3", ["command1", "command2"]),
       ("VM4", "command4", ["command3"])
   ]
   expected_output = [
       ("VM1", "command1", []),
       ("VM2", "command2", ["command1"]),
       ("VM3", "command3", ["command1", "command2"]),
       ("VM4", "command4", ["command3"])
   ]
   assert resolve_command_order(commands) == expected_output

   # Test case 4: Empty input
   commands = []
   expected_output = []
   assert resolve_command_order(commands) == expected_output


test_resolve_command_order()
