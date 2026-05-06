class MinStack:

    def __init__(self):

        self.array = []
        

    #push to top of stack 
    def push(self, val: int) -> None:
        self.array.append(val)
        

    def pop(self) -> None:
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
#get min -> 