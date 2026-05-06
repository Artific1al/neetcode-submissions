#struggled with this one - mentally OUT of it.

class MinStack:

    def __init__(self):

        self.array = []
        self.minStack = []
        

    #push to top of stack 
    def push(self, val: int) -> None:
        #if minStack empty
        if not self.minStack:
            self.minStack.append(val)
        
        #if minStack populated
        else:
            #prev minimum

            lowest = self.minStack[-1]
            lowest = val if val < lowest else lowest 
            self.minStack.append(lowest)

        self.array.append(val)


    def pop(self) -> None:
        #if this is the min element
        self.array.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.array[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]

    
#constraints
#O(1) functions
#O(n) space

#bruteforce 
#get min -> O(n) searc

#edge cases
#