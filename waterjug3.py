def pour_water(jug1, jug2, capacity1, capacity2, target, visited=set()):
    print("Jug1:", jug1, "Jug2:", jug2)
    
    if jug1 == target or jug2 == target:
        print("Target reached!")
        return True
    
    visited.add((jug1, jug2))
    
    options = [(capacity1, jug2), (jug1, capacity2), (0, jug2), (jug1, 0),
               (max(0, jug1 - (capacity2 - jug2)), min(jug2 + jug1, capacity2)),
               (min(jug1 + jug2, capacity1), max(0, jug2 - (capacity1 - jug1)))]
    
    for option in options:
        if option not in visited and pour_water(*option, capacity1, capacity2, target, visited):
            return True
    
    return False

jug1_capacity = 4
jug2_capacity = 3
target_amount = 2

print("Steps:")
pour_water(0, 0, jug1_capacity, jug2_capacity, target_amount)

