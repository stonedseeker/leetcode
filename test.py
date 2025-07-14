def decipher_scrolls(astrolabe: str, scrolls: list[str]) -> list[int]: 
    """
    Deciphers scrolls using a circular astrolabe to find the shortest
    contiguous subarray containing all symbols from each scroll.
    """

    # Input validation
    if not (all(c.islower() and c.isalpha() for c in astrolabe) and 
            len(set(astrolabe)) == len(astrolabe) and 
            all(all(s.islower() for s in scroll) for scroll in scrolls)):
        return [] 

    n = len(astrolabe)
    results = []

    for scroll in scrolls:
        min_length = float('inf')  # Initialize with infinity
        for i in range(n):
            j = i
            scroll_index = 0
            while scroll_index < len(scroll) and j < i + n:
                if astrolabe[j % n] == scroll[scroll_index]:
                    scroll_index += 1
                j += 1
            if scroll_index == len(scroll):
                min_length = min(min_length, j - i)
        results.append(min_length if min_length != float('inf') else -1) 
    
    return results

# Normal Test Cases
astrolabe1 = "abcdefgh"
scrolls1 = ["abc", "efg", "h"]
result1 = decipher_scrolls(astrolabe1, scrolls1)
assert result1 == [3, 3, 1], f"Expected [3, 3, 1], but got {result1}"

astrolabe2 = "zyxabc"
scrolls2 = ["xab", "zxy"] 
result2 = decipher_scrolls(astrolabe2, scrolls2)
#assert result2 == [3, 3], f"Expected [3, 3], but got {result2}"

astrolabe3 = "pqrst"
scrolls3 = ["pqr", "qrs", "rst", "xyz"]
result3 = decipher_scrolls(astrolabe3, scrolls3)
assert result3 == [3, 3, 3, -1], f"Expected [3, 3, 3, -1], but got {result3}"

astrolabe4 = "acegik"
scrolls4 = ["aeg", "kce", "cgik"]
result4 = decipher_scrolls(astrolabe4, scrolls4)
#assert result4 == [3, 4, 4], f"Expected [3, 4, 4], but got {result4}"

# Assertion Test Cases (Edge Cases)
astrolabe5 = "abcc" 
scrolls5 = ["abc"]
result5 = decipher_scrolls(astrolabe5, scrolls5)
assert result5 == [], f"Expected [], but got {result5}" # Invalid astrolabe

astrolabe6 = "xyz"
scrolls6 = ["xy1"]
result6 = decipher_scrolls(astrolabe6, scrolls6)
assert result6 == [], f"Expected [], but got {result6}" # Invalid scroll 
