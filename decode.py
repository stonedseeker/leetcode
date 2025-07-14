class DanceScorer:
    def __init__(self, movements):
        if not isinstance(movements, list):
            raise ValueError("Movements must be a list")
        if not all(isinstance(x, int) for x in movements):
            raise ValueError("All movements must be integers")
        if len(movements) < 3:
            raise ValueError("Routine must have at least 3 movements")
        
        self.movements = movements
        self.n = len(movements)
        self.flow_cache = {}
    
    def analyze_flow_sequence(self, start, length):
        if not 0 <= start < self.n or not 1 <= length <= self.n - start:
            raise ValueError("Invalid sequence parameters")
        
        cache_key = (start, length)
        if cache_key in self.flow_cache:
            return self.flow_cache[cache_key]
        
        sequence = self.movements[start:start+length]
        
        # Calculate flow score
        flow_score = 0
        for i in range(1, len(sequence)):
            transition = abs(sequence[i] - sequence[i-1])
            if (sequence[i] > 0) == (sequence[i-1] > 0):
                flow_score += transition * 2
            else:
                flow_score += transition // 2
        
        # Apply multipliers
        if all(x > 0 for x in sequence):
            flow_score *= 1.5
        elif all(x < 0 for x in sequence):
            flow_score *= 1.2
        
        flow_score = int(flow_score) % 10000
        self.flow_cache[cache_key] = flow_score
        return flow_score
    
    def find_highlight_moments(self):
        highlights = []
        for i in range(self.n - 2):
            if self.is_highlight_moment(i):
                score = sum(abs(x) for x in self.movements[i:i+3])
                highlights.append((i, score))
        return sorted(highlights, key=lambda x: -x[1])
    
    def is_highlight_moment(self, index):
        if index + 2 >= self.n:
            return False
        
        a, b, c = self.movements[index:index+3]
        # Check for special combinations
        return (abs(a) < abs(b) > abs(c) or  # Peak
                abs(a) > abs(b) < abs(c) or  # Valley
                (a < 0 and b > 0 and c < 0) or  # Zigzag negative
                (a > 0 and b < 0 and c > 0))    # Zigzag positive
    
    def calculate_rhythm_pattern(self):
        pattern_score = 0
        for i in range(self.n - 1):
            for j in range(i + 1, min(i + 4, self.n)):
                diff = abs(self.movements[j] - self.movements[i])
                if diff % 3 == 0:
                    pattern_score += diff // 3
                elif diff % 2 == 0:
                    pattern_score += diff // 2
        return pattern_score % 10000
    
    def artistic_score(self):
        # Combine different aspects for final score
        flow_total = sum(self.analyze_flow_sequence(i, 3) 
                         for i in range(self.n - 2))
        highlight_scores = [score for _, score in self.find_highlight_moments()]
        highlight_total = sum(highlight_scores[:3]) if highlight_scores else 0
        rhythm_score = self.calculate_rhythm_pattern()
        
        final_score = (flow_total * 3 + highlight_total * 2 + rhythm_score) % 1000000
        return final_score

def run_test_case(movements, expected_results):
    print(f"Test case for movements: {movements}")
    try:
        scorer = DanceScorer(movements)
        results = {
            'flow3_0': scorer.analyze_flow_sequence(0, 3),
            'highlights': len(scorer.find_highlight_moments()),
            'rhythm': scorer.calculate_rhythm_pattern(),
            'artistic': scorer.artistic_score()
        }
        for key, expected in expected_results.items():
            assert results[key] == expected, f"Failed {key}: got {results[key]}, expected {expected}"
        print("All assertions passed")
        return True
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

# Test Case 1
movements1 = [3, -2, 5, 4, -1, 6]
scorer1 = DanceScorer(movements1)
print("Test Case 1:")
print(f"Movements: {movements1}")
print(f"Flow Sequence (0,3): {scorer1.analyze_flow_sequence(0, 3)}")
print(f"Highlight Moments: {len(scorer1.find_highlight_moments())}")
print(f"Rhythm Pattern: {scorer1.calculate_rhythm_pattern()}")
print(f"Artistic Score: {scorer1.artistic_score()}")
print("---")

# Test Case 2
movements2 = [1, 2, 3, 4, 5]
scorer2 = DanceScorer(movements2)
print("Test Case 2:")
print(f"Movements: {movements2}")
print(f"Flow Sequence (0,3): {scorer2.analyze_flow_sequence(0, 3)}")
print(f"Highlight Moments: {len(scorer2.find_highlight_moments())}")
print(f"Rhythm Pattern: {scorer2.calculate_rhythm_pattern()}")
print(f"Artistic Score: {scorer2.artistic_score()}")
print("---")

# Test Case 3
movements3 = [-4, 6, -2, 8, -5]
scorer3 = DanceScorer(movements3)
print("Test Case 3:")
print(f"Movements: {movements3}")
print(f"Flow Sequence (0,3): {scorer3.analyze_flow_sequence(0, 3)}")
print(f"Highlight Moments: {len(scorer3.find_highlight_moments())}")
print(f"Rhythm Pattern: {scorer3.calculate_rhythm_pattern()}")
print(f"Artistic Score: {scorer3.artistic_score()}")
print("---")

# Test Case 4
movements4 = [10, -10, 10, -10, 10]
scorer4 = DanceScorer(movements4)
print("Test Case 4:")
print(f"Movements: {movements4}")
print(f"Flow Sequence (0,3): {scorer4.analyze_flow_sequence(0, 3)}")
print(f"Highlight Moments: {len(scorer4.find_highlight_moments())}")
print(f"Rhythm Pattern: {scorer4.calculate_rhythm_pattern()}")
print(f"Artistic Score: {scorer4.artistic_score()}")
print("---")

# Test Case 5
movements5 = [1, 1, 1, -1, -1]
scorer5 = DanceScorer(movements5)
print("Test Case 5:")
print(f"Movements: {movements5}")
print(f"Flow Sequence (0,3): {scorer5.analyze_flow_sequence(0, 3)}")
print(f"Highlight Moments: {len(scorer5.find_highlight_moments())}")
print(f"Rhythm Pattern: {scorer5.calculate_rhythm_pattern()}")
print(f"Artistic Score: {scorer5.artistic_score()}")
print("---")

# Test Case 6
movements6 = [-5, -4, -6, -3, -7]
scorer6 = DanceScorer(movements6)
print("Test Case 6:")
print(f"Movements: {movements6}")
print(f"Flow Sequence (0,3): {scorer6.analyze_flow_sequence(0, 3)}")
print(f"Highlight Moments: {len(scorer6.find_highlight_moments())}")
print(f"Rhythm Pattern: {scorer6.calculate_rhythm_pattern()}")
print(f"Artistic Score: {scorer6.artistic_score()}")
print("---")

# Test Case 7
movements7 = [2, -3, 4, -5, 6]
scorer7 = DanceScorer(movements7)
print("Test Case 7:")
print(f"Movements: {movements7}")
print(f"Flow Sequence (0,3): {scorer7.analyze_flow_sequence(0, 3)}")
print(f"Highlight Moments: {len(scorer7.find_highlight_moments())}")
print(f"Rhythm Pattern: {scorer7.calculate_rhythm_pattern()}")
print(f"Artistic Score: {scorer7.artistic_score()}")
print("---")

# Test Case 8
movements8 = [7, 3, 7, 3, 7]
scorer8 = DanceScorer(movements8)
print("Test Case 8:")
print(f"Movements: {movements8}")
print(f"Flow Sequence (0,3): {scorer8.analyze_flow_sequence(0, 3)}")
print(f"Highlight Moments: {len(scorer8.find_highlight_moments())}")
print(f"Rhythm Pattern: {scorer8.calculate_rhythm_pattern()}")
print(f"Artistic Score: {scorer8.artistic_score()}")
print("---")

# Test Case 9
movements9 = [-1, -2, -1, -2, -1]
scorer9 = DanceScorer(movements9)
print("Test Case 9:")
print(f"Movements: {movements9}")
print(f"Flow Sequence (0,3): {scorer9.analyze_flow_sequence(0, 3)}")
print(f"Highlight Moments: {len(scorer9.find_highlight_moments())}")
print(f"Rhythm Pattern: {scorer9.calculate_rhythm_pattern()}")
print(f"Artistic Score: {scorer9.artistic_score()}")
print("---")

# Test Case 10
movements10 = [5, 0, 5, 0, 5]
scorer10 = DanceScorer(movements10)
print("Test Case 10:")
print(f"Movements: {movements10}")
print(f"Flow Sequence (0,3): {scorer10.analyze_flow_sequence(0, 3)}")
print(f"Highlight Moments: {len(scorer10.find_highlight_moments())}")
print(f"Rhythm Pattern: {scorer10.calculate_rhythm_pattern()}")
print(f"Artistic Score: {scorer10.artistic_score()}")
print("---")

# Input validation tests
print("\nInput Validation Tests:")
try:
    DanceScorer("not a list")
except ValueError as e:
    print(f"Test 1: {str(e)}")

try:
    DanceScorer([1, 2, "3"])
except ValueError as e:
    print(f"Test 2: {str(e)}")

try:
    DanceScorer([1, 2])
except ValueError as e:
    print(f"Test 3: {str(e)}")
