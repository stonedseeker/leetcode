def pour_water(jug1, jug2, capacity1, capacity2, target):
    print("Jug1:", jug1, "Jug2:", jug2)
    
    if jug1 == target or jug2 == target:
        print("Target reached!")
        return True
    
    visited_states.add((jug1, jug2))
    
    # Fill jug1
    if jug1 < capacity1 and (capacity1, jug2) not in visited_states:
        if pour_water(capacity1, jug2, capacity1, capacity2, target):
            return True
    
    # Fill jug2
    if jug2 < capacity2 and (jug1, capacity2) not in visited_states:
        if pour_water(jug1, capacity2, capacity1, capacity2, target):
            return True
    
    # Pour jug1 to jug2
    if jug1 > 0 and jug2 < capacity2:
        pour_amount = min(jug1, capacity2 - jug2)
        if (jug1 - pour_amount, jug2 + pour_amount) not in visited_states:
            if pour_water(jug1 - pour_amount, jug2 + pour_amount, capacity1, capacity2, target):
                return True
    
    # Pour jug2 to jug1
    if jug2 > 0 and jug1 < capacity1:
        pour_amount = min(jug2, capacity1 - jug1)
        if (jug1 + pour_amount, jug2 - pour_amount) not in visited_states:
            if pour_water(jug1 + pour_amount, jug2 - pour_amount, capacity1, capacity2, target):
                return True
    
    # Empty jug1
    if jug1 > 0 and (0, jug2) not in visited_states:
        if pour_water(0, jug2, capacity1, capacity2, target):
            return True
    
    # Empty jug2
    if jug2 > 0 and (jug1, 0) not in visited_states:
        if pour_water(jug1, 0, capacity1, capacity2, target):
            return True
    
    return False

visited_states = set()
jug1_capacity = 4
jug2_capacity = 3
target_amount = 2

print("Steps:")
pour_water(0, 0, jug1_capacity, jug2_capacity, target_amount)

