from collections import deque

class Truck():

    def __init__(self, weight, time):

        self.weight = weight
        self.time = time


def solution(bridge_length, weight, truck_weights):
    seconds = 0
    totalWeights = 0
    moving = deque()
    trucks = deque(truck_weights)
    
    while moving or trucks:

        if moving and (seconds - moving[0].time) == bridge_length:
            totalWeights -= moving[0].weight
            moving.popleft()
        
        if trucks and (totalWeights + trucks[0]) <= weight:
            totalWeights += trucks[0]
            moving.append(Truck(trucks[0], seconds))
            trucks.popleft()
        
        seconds += 1

    return seconds

print(solution(2, 10, [7, 4, 5, 6]))