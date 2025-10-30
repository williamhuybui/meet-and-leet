class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def finish_all(piles, h, speed) -> bool:
            actual_time = 0
            for p in piles:
                if p/speed > p//speed:
                    actual_time += p//speed + 1
                else:
                    actual_time += p//speed
            # print(actual_time)
            return actual_time <= h

        # finish_all(piles, h, 6)    
        min_speed, max_speed = 1, max(piles)
        while min_speed < max_speed:
            avg_speed = (min_speed + max_speed)//2
            if finish_all(piles, h, avg_speed):
                max_speed = avg_speed
            else:
                min_speed = avg_speed + 1
        return min_speed

# Time complexity: log(max(piles)) * len(piles)
