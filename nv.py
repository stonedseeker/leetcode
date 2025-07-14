def decrypt_number(num, damage, threshold):
    operations = 0
    while num > 1 and damage < threshold:
        if num % 2 == 0:
            num //= 2
            damage += 1
        elif num % 3 == 0:
            num //= 3
            damage += 2
        elif num % 5 == 0:
            num //= 5
            damage += 3
        else:
            num -= 1
            damage += 1
        operations += 1
    return num == 1, damage, operations

def decrypt_scroll(encrypted_nums, damage_threshold):
    if not isinstance(damage_threshold, int) or damage_threshold < 0:
        raise ValueError("Damage threshold must be a non-negative integer")
    if not all(isinstance(num, int) and num > 0 for num in encrypted_nums):
        raise ValueError("All encrypted numbers must be positive integers")

    decrypted_count = 0
    decrypted_chars = []
    total_damage = 0

    for num in encrypted_nums:
        success, new_damage, ops = decrypt_number(num, total_damage, damage_threshold)
        if success:
            decrypted_count += 1
            decrypted_chars.append(ops)
        total_damage = new_damage
        if total_damage >= damage_threshold:
            break

    return decrypted_count, decrypted_chars, total_damage

# Test cases
encrypted_nums1 = [4, 9, 25, 17, 12, 8]
threshold1 = 10
assert decrypt_scroll(encrypted_nums1, threshold1) == (3, [2, 2, 2], 12)

encrypted_nums2 = [100, 200, 300, 400, 500]
threshold2 = 50
assert decrypt_scroll(encrypted_nums2, threshold2) == (5, [4, 5, 5, 6, 5], 48)

encrypted_nums3 = [7, 11, 13, 17, 19, 23]
threshold3 = 15
assert decrypt_scroll(encrypted_nums3, threshold3) == (3, [3, 3, 4], 15)

encrypted_nums4 = [64, 81, 125, 16, 27, 125]
threshold4 = 30
assert decrypt_scroll(encrypted_nums4, threshold4) == (4, [6, 4, 3, 4], 31)

encrypted_nums5 = [2, 3, 5, 7, 11, 13, 17, 19]
threshold5 = 20
assert decrypt_scroll(encrypted_nums5, threshold5) == (6, [1, 1, 1, 3, 3, 4], 20)

encrypted_nums6 = [1000, 999, 998, 997, 996]
threshold6 = 100
assert decrypt_scroll(encrypted_nums6, threshold6) == (5, [6, 8, 11, 11, 10], 66)

encrypted_nums7 = [31, 33, 35, 37, 39, 41]
threshold7 = 25
assert decrypt_scroll(encrypted_nums7, threshold7) == (3, [4, 4, 4], 26)

encrypted_nums8 = [128, 256, 512, 1024, 2048]
threshold8 = 40
assert decrypt_scroll(encrypted_nums8, threshold8) == (4, [7, 8, 9, 10], 40)

encrypted_nums9 = [15, 30, 45, 60, 75, 90]
threshold9 = 35
assert decrypt_scroll(encrypted_nums9, threshold9) == (5, [2, 3, 3, 4, 3], 36)

encrypted_nums10 = [101, 202, 303, 404, 505]
threshold10 = 60
assert decrypt_scroll(encrypted_nums10, threshold10) == (5, [5, 6, 6, 7, 6], 53)

# Input validation test cases
try:
    decrypt_scroll([1, 2, 3], -1)
except ValueError as e:
    assert str(e) == "Damage threshold must be a non-negative integer"

try:
    decrypt_scroll([1, 2, "3"], 10)
except ValueError as e:
    assert str(e) == "All encrypted numbers must be positive integers"

try:
    decrypt_scroll([1, 2, 0], 10)
except ValueError as e:
    assert str(e) == "All encrypted numbers must be positive integers"

print("All test cases passed!")
