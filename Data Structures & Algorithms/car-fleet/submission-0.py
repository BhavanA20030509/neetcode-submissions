class Solution:
    def carFleet(self, target, position, speed):
        cars=sorted(zip(position,speed),reverse=True)
        fleet=0
        fleet_time=0
        for position,speed in cars:
            time=(target-position)/speed
            if time>fleet_time:
                fleet+=1
                fleet_time=time
        return fleet
        