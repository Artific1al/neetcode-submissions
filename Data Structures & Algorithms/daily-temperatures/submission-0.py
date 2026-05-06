class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        output = [0] * len(temperatures)

        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    output[i] = j-i
                    break
        
        return output


#Idea - using stack to build temperature up to this point array
#Input: [30,38,30,36,35,40,28]
#Output: [1,4,1,2,1,0,0]
#SoFar: [30, 38, 38, 38, 40, 40]




















        # descendingStack = []
        # output = [0] * len(temperatures)

        # #iterate through every num using stacks to reduce repeat work
        # for i in range(0, len(temperatures)-2): 
        #     num = temperatures[i]
        #     nextIndex = i

        #     #until we find a num bigger than current and while in range 
        #     while num <= temperatures[nextIndex] and nextIndex <= len(temperatures -1):
        #         nextIndex +=1
        #         nextNum = temperatures[nextIndex]

        #         #case 1: immediate number is bigger:
        #         if nextNum > num:
        #             output[i] = 1
                
        #         #case 2: immediate num is smaller and we have a stack
        #         elif descendingStack and nextNum <= num:
        #             bigger = True # the num at nextIndex is bigger than the top of the descendingStack
        #             while descendingStack and bigger:
        #                 topOfStack = descendingStack.pop()

        #                 #case 2.1 nextNum is > topOfStack
        #                 if nextNum > topOfStack:
        #                     output[nextIndex] = 1

        #                 #case 2.2 nextNum is < topOfStack    
        #                 else:
        #                     descendingStack.append(nextNum)



                
        #         #case 3: immediate num is smaller and no stack
        #         else:
        #             descendingStack.append(nextNum)
            
        #     #edgecase - end of list leave everything else as 0 because of the invariant
        #     #that everything in the stack must be in descending order 

        # return output




#Constraints
# list len 1-1000
# individual temperatures ints between 1-100
# time and space O(n)

#Brute Force
#manually search through entire array every time O(n^2 time)

#Edge Cases
#if list = len(1) reutnr [0]
#if you get to hottest temperature then 0 for that index

#Is there any repeated work?
#[]
#current = 1

#Idea - using stack to build temperature up to this point array
#Input: [30,38,30,36,35,40,28]
#Output: [1,4,1,2,1,0,0]
#SoFar: [30, 38, 38, 38, 40, 40]

#what if every time I find a num I do this:
#if the next num is greater: fantastic:
#else: create a stack and add that num <- maintain the sorted nature of this such that the thing
#on the top of the stack is always the smallest
#then for every consecutive jump, if the current num is bigger then pop the first thing off the stack
#and keep doing so until either stack is empty and current num is smaller than new num

#[#Input: [30,38,30,36,35,40,28]
#Output: [1,0, 1, 0 , 0, 0, 0 ]
#Stack
#@ 38 -> 30, numINd = 1, curInd = 2 smaller so add to staack
#Stack = [30]
#@38 -> 36, numInd = 1, curInd = 3 smaller so pop until a num is smaller
#30 < 36 so curInd output num = 1, add 36 to stack
#Stack = [36]
#@38 -> 35, numInd = 1, curInd = 4, smaller so pop until a num is smaller
#38 > 35 so pop until stack is smaller, 36 is > 35 so append 36 then 35
#Stack = [36, 35]
#@38 -> 40, numInd = 1, curInd = 5, bigger! Clear stack. numInd outPut = curInd - numInd = 4
#Stack = [36, 35] , 

#how do we know the indices are curInd -1 and -2, because OTHERWISE
#they would have been taken off the stack by now
#they can only be on the stack if smaller than 38 and smaller than prev num i.e. must be a sorted 
#descending list in THAT order

#ouptput = [1, 4, 1, 2, 1]

#40 -> 28
#what to do with stack? must all be descending i.e. all set to 0