class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for pair in zip(position, speed):
            cars.append(pair)
        
        cars = sorted(cars, reverse=True)

        curr_ahead = None
        num_fleets = 1

        for car in cars:
            reach = (target - car[0])/car[1]
            if curr_ahead is not None:
                if reach > curr_ahead:
                    num_fleets += 1
                    curr_ahead = reach
            else:
                curr_ahead = reach
        
        return num_fleets

