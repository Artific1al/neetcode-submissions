##Struggling
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # cars = []
        # for i in range(len(positions)):
        #     time = position[i]
        #     cars.append()
        







        cars = []
        for i in range(len(position)):
            cars.append((position[i], ((target-position[i]) / speed[i])))
        
        #sort by positions
        sortedCars = sorted(cars, key= lambda car: car[0], reverse=True)
        fleets = []

        for car in sortedCars:
            #always append first car -> there will always be at least one fleet
            if len(fleets) == 0:
                fleets.append(car)
            
            
            #if car behind current is faster and will catch up
            elif car[1] <= fleets[-1][1]:
                continue

            elif car[1] > fleets[-1][1]:
                fleets.append(car)           

        return len(fleets)

        
        
        # target = 10, position = [4,1,0,7], speed = [2,2,1,1]
        # Expected = [3, 5, 10, 3]

        # position = [0,1,4,7], speed = [1, 2, 2, 1]
        # cars = [(0, 2), (1, 1), (4,2), (7, 1)]
        # y = 2x + 0
        # y = 1x + 1
        
        
        
        
            
        
        
        
        # #Series of floats representing when a car will finish
        # time = [0] * len(position)
        # fleets = 0

        # #O(n) passover to determine how long it will take each car
        # for carInd in range(len(position)-1, -1, -1):
        #     pos = position[carInd]
        #     speed = position[carInd]
        #     time[carInd] = (target - position) / speed
            
        # stack = []
        # stack.append(position)[-1]


        # while position:

        #     endPosition = position.pop()
        #     endSpeed = speed.pop()  
        #     timeToHitTarget = (target - endPosition) / endSpeed 



#Constraints
#Non empty -> between 1 and 1000 cars
#N = len(position) = len(speed)
#Target: Betwen 1 and 1000
#Speed: Between 1 and 100
#All values of position are unique -> two cars can start behind each other (3,4) but not in same spot
#(4,4)
# n log n time, n space


#Brute Force #O(n)
#For position[-1] calculate how long until it hits the target #O(1)
#Then, for every car after it do same calculation until a car would not hit the end #O(1) * x
#As fast or faster than position[-1]
#Increment count, pop all those off of position and speed

#Edge cases

#Optimisation
#Start from the end, have a list of currentPos and currentSpeed
#Add the end car to a stack, and calculate the time till end
#Iterate backwards from end - while currentArrival <= endArrival, pop
#Once you get to one that doesnt -> pop all up to that point, incremment fleets

#Then, you need to recalculate positions O(n^2)
