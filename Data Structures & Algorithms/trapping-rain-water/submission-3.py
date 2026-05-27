##didnt figure out myself

class Solution:

     def trap(self, height: List[int]) -> int:
        #Two Pointers Starting at the start of the array
        #One Pointer (P1) will go right while comparing itself to the height of the other pointer (P2)
        # P1 will compare its height to P2
        # If P1 current traversed height is smaller than P2's height, it will append that height to stack and keep going
        # Once P1 finds a height the same size or bigger than P2, it will do an area calculation 
        # Area calc: Whichever pointer has the smaller height * Index of P1 - Index of P2
        # Then you would deduct all the values in the stack from the area calc to find the are of the trapped rain water
        # You would store that in a value called the biggest if its bigger than the previous calc
        # You would then put P2 at the same position as P1, Empty the stack, and do it all over again until the P1 reaches the end.
        water = 0
        p2 = 0
        stack = []

        # skip leading zeros
        water = 0
        p2 = 0
        stack = []

        while p2 < len(height) and height[p2] == 0:
            p2 += 1

        p1 = p2 + 1
        while p1 < len(height):
            if height[p1] >= height[p2]:
                effective_h = min(height[p1], height[p2])
                water += effective_h * (p1 - p2 - 1) - sum(stack)
                p2 = p1
                stack = []
            else:
                stack.append(height[p1])
            p1 += 1

        # right pass: start from the RIGHT END, stop when we reach p2
        last_p2 = p2
        p2 = len(height) - 1
        stack = []

        p1 = p2 - 1
        while p1 >= last_p2:
            if height[p1] >= height[p2]:
                effective_h = min(height[p1], height[p2])
                water += effective_h * (p2 - p1 - 1) - sum(stack)
                p2 = p1
                stack = []
            else:
                stack.append(height[p1])
            p1 -= 1

        return water
    #  def trap(self, height):

    #     left = 0
    #     right = 0
    #     best = 0

    #     #edge case - no water unless inbetween two walls
    #     while height[left] == 0 and left+1 <= len(height)-1:
    #         left +=1
    #     right = left


    #     monotonic = []
    #     last_check_ind

    #     while right <= len(height)-1:
            
    #         #the current we are trying to match or exceed
    #         cHeight = height[left]
            
    #         #edge case first val
    #         if not monotonic:
    #             monotonic.append(cHeight)
    #             right +=1

    #         #for all non-first steps, check the next
    #         else:
    #             rHeight = height[right]

    #             #case 1 rHeight < cHeight - we cannot "calculate" so add to stack
    #             if rHeight < cHeight:
    #                 monotonic.append(rHeight)
    #                 right +=1
                
    #             #case 2 rHeight >= cHeight - we can calculate so pop from stack
    #             else:
    #                 area = cHeight * (right - left)
    #                 while monotonic:
    #                     area -= monotonic.pop()
    #                 best += area
    #                 left = right
    #                 last_check_ind = 
        


    #     return best