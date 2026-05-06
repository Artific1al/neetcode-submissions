class MinStack:

    def __init__(self):

        self.array = []
        self.minIndex = 0
        

    #push to top of stack 
    def push(self, val: int) -> None:
        #if this is new min element -> point to it
        if self.array and self.array[self.minIndex] > val:
            self.minIndex = len(self.array)

        self.array.append(val)


    def pop(self) -> None:
        #if this is the min element
        if self.minIndex == len(self.array) -1:
            self.minIndex = 0

            for index in range(len(self.array)-1):
                if self.array[index] < self.array[self.minIndex]:
                    self.minIndex = index  

        self.array.pop()
        

    def top(self) -> int:
        return self.array[-1]
        

    def getMin(self) -> int:
        elem = self.array[0]
        for num in self.array:
            if num < elem:
                elem = num

        return elem

    
#constraints
#O(1) functions
#O(n) space

#bruteforce 
#get min -> O(n) searc