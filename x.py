from collections import defaultdict
from datetime import datetime

class WeatherData:
    def __init__(self):
        self.data = {}  # Store measurements as {timestamp: (temperature, humidity)}

    def insert(self, temperature: float, humidity: float, timestamp: str) -> None:
        if not self._is_valid_timestamp(timestamp):
            raise ValueError("Invalid timestamp.")
        self.data[timestamp] = (temperature, humidity)

    def remove(self, timestamp: str) -> None:
        if timestamp not in self.data:
            raise ValueError("Timestamp not found.")
        del self.data[timestamp]

    def query_average(self, start: str, end: str) -> tuple[float, float]:
        if not self._is_valid_timestamp(start) or not self._is_valid_timestamp(end) or start > end:
            raise ValueError("Invalid time range.")

        total_temp = total_hum = count = 0
        for ts, (temp, hum) in self.data.items():
            if start <= ts <= end:
                total_temp += temp
                total_hum += hum
                count += 1
        
        if count == 0:
            return (0.0, 0.0)  # No data in range

        return (total_temp / count, total_hum / count)

    def _is_valid_timestamp(self, timestamp: str) -> bool:
        try:
            datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
            return True
        except ValueError:
            return False









# Test Case #1: Basic functionality
wd = WeatherData()
wd.insert(20.5, 30.0, '2024-09-24 12:30:00')
wd.insert(22.0, 35.0, '2024-09-24 12:45:00')
wd.insert(21.0, 33.0, '2024-09-24 13:15:00')
avg_temp, avg_hum = wd.query_average('2024-09-24 12:00:00', '2024-09-24 13:00:00')
assert avg_temp == 21.25  # Expected average temperature
assert avg_hum == 32.5     # Expected average humidity

# Test Case #2: Removing a measurement
wd.remove('2024-09-24 12:45:00')
avg_temp, avg_hum = wd.query_average('2024-09-24 12:00:00', '2024-09-24 13:00:00')
assert avg_temp == 20.5  # Expected updated average temperature
assert avg_hum == 30.0   # Expected updated average humidity

# Test Case #3: Querying with no data in range
avg_temp, avg_hum = wd.query_average('2024-09-24 14:00:00', '2024-09-24 15:00:00')
assert avg_temp == 0.0  # Expected: No data
assert avg_hum == 0.0   # Expected: No data

# Test Case #4: Error handling for invalid timestamp on remove
try:
    wd.remove('2024-09-24 14:00:00')
except ValueError as e:
    assert str(e) == "Timestamp not found."  # Expected error message

# Test Case #5: Error handling for query with invalid range
try:
    wd.query_average('2024-09-24 13:00:00', '2024-09-24 12:00:00')
except ValueError as e:
    assert str(e) == "Invalid time range."  # Expected error message

