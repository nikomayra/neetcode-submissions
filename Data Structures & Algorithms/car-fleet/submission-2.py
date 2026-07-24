class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = sorted(zip(position, speed), reverse=True)
        # print (pos_speed)

        car_fleets_times = []

        for pos, sp in pos_speed:
            time = (target - pos) / sp
            if car_fleets_times and car_fleets_times[-1] >= time:
                continue
            else:
                car_fleets_times.append(time)
        
        # print(car_fleets_times)
        return len(car_fleets_times)