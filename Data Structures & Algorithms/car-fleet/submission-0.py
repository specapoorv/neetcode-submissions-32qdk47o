class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        paired = list(zip(position, speed))
        paired.sort(key = lambda x : x[0])
        position, speed = zip(*paired)
        times = []
        fleet = 0
        for i, position in enumerate(position):
            dist = target - position 
            time = (dist / speed[i])
            times.append(time)
        
        highest_time = 0
        while len(times):
            time = times[-1]
            if time>highest_time:
                highest_time = time
                fleet +=1 
            times.pop()

        return fleet
