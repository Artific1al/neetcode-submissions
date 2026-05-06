class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        output = [0] * len(temperatures)
        stack = []
        for index, element in enumerate(temperatures):
                #if its bigger than anything in stack then remove them all
                while stack and element > stack[-1][1]:
                    top = stack.pop()
                    output[top[0]] = index - top[0]
                
                stack.append((index, element))

        return output

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # descendingStack = []
        # output = [0] * len(temperatures)
        # finished = False

        # #iterate through every num using stacks to reduce repeat work
        # for i in range(0, len(temperatures)-2): 
            
        #     if output[i] >0:
        #         continue

        #     if finished:
        #         break

        #     num = temperatures[i]
        #     nextIndex = i+1

        
        #     nextNum = temperatures[nextIndex]
        #     assigned = False

        #     #until we find a num bigger than current and while in range 
        #     while num >= temperatures[nextIndex] and nextIndex <= len(temperatures) -1 and not assigned:

        #         #if at end of list - return from all loops
        #         #if nextIndex == len(temperatures) -1:
        #         #    finished = True
        #         #    break
                
                
        #         #case 1: immediate number is bigger:
        #         if nextNum > num:
        #             output[i] = 1
        #             assigned = True
                
        #         #case 2: immediate num is smaller and we have a stack
        #         elif descendingStack and nextNum <= num:
        #             bigger = True # the num at nextIndex is bigger than the top of the descendingStack
        #             stackSize = len(descendingStack)
        #             while descendingStack and bigger:
        #                 topOfStack = descendingStack.pop()

        #                 #case 2.1 nextNum is > topOfStack
        #                 if nextNum > topOfStack:
        #                     stackSizeNow = len(descendingStack)
        #                     distance = nextIndex - (stackSize - stackSizeNow)
        #                     output[distance] = (stackSize - stackSizeNow)

        #                     if len(descendingStack) == 0:
        #                         descendingStack.append(nextNum)
        #                         bigger = False
                            
        #                 #case 2.2 nextNum is < topOfStack    
        #                 else:
        #                     descendingStack.append(topOfStack)
        #                     descendingStack.append(nextNum)
        #                     bigger = False



                
        #         #case 3: immediate num is smaller and no stack
        #         else:
        #             descendingStack.append(nextNum)
            
        #         #increment next num
        #         if nextIndex+1 <= (len(temperatures)-1):
        #             nextIndex +=1
        #             nextNum = temperatures[nextIndex]
        #         else:
        #             return output

        #     #this iteration there was no loop because next num is bigger
        #     if assigned == False and not descendingStack:
        #         output[i] = 1

        #     #bigger number, empty whole stack:
        #     elif assigned == False and descendingStack:
        #         for k in range(nextIndex -1, nextIndex - len(descendingStack)-1, -1):
        #             output[k] = nextIndex - k
                
        #         output[i] = nextIndex - i
        #         assigned = True


        #     #edgecase - end of list leave everything else as 0 because of the invariant
        #     #that everything in the stack must be in descending order 

        # return output
        