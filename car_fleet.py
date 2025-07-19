class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pos_speed = sorted([(x, y) for x,y in zip(position, speed)], reverse=True)
        
        print(pos_speed)
        fleet = 0
        last_time = 0

        for pos, spd in pos_speed:
            time = (target - pos) / spd
            print(time, last_time)
            if time > last_time:
                last_time = time
                fleet += 1
        
        return fleet

