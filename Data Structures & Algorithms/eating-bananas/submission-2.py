class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        k = (l + r) // 2 #mid
        mink = r #minimum k

        while l <= r:

            #calc hours new k takes
            current = 0
            for elem in piles:
                current += elem // k if (elem % k == 0) else elem // k + 1 #
            
            #too many hours - make k bigger
            if current > h:
                l = k + 1
                k = (l+r) // 2
            
            #this value of k works - but can we make it smaller?
            elif current <= h and k < mink:
                mink = k
                r = k-1
                k = (l+r) // 2
            
            #current < h and k >= mink
            else:
                return mink

        return mink

#-- DID NOT RUN THROUGH EXAMPLE BEFORE HITTING RUN - THIS ONES HARD.


            ##lower k if required
            #if current <=h and current < mink:
            #    mink = current
            

            #binary search
            #if k

        # if current > h
        # - make bigger

        # if current < h
        # - see if smaller k does the job

        #-- needed all 5 hints
        #at first mis-read question to think find the values of k that minimises the number
        #of hours required to eat - this is NOT the question
        #I then thought you'd have to sort but you don't have the time to sort nor is it necessary
        

#constraints
#O n log m time | O1 space
#n input array, m max value
#k < h

#edge cases
#one pile -> return piles[0]

#brute force
#pick largest number <= h and iterate down through the array checking num-1 each time
#linear search O(n^2) time | O(1) space

#idea
#if sorted (n log m?)
#linear search to find first number that exceeds h - this is max, piles[0][sorted] is min
#then do a binary search and each time track designate mid of bin search as k
#then, for every value in piles modulo w k and sum up this - this is the mid_value
#if mid_value can go smaller -> go down / decrease the binary search - go that way

#Return the minimum integer k such that you can eat all the bananas within h hours.

#1 2 2 4 5 h = 12
#k=1 - 12
#k=2 - 8
#k=4 - 6
#k=5 - 5
#10 25 45 70 200
#

#n log m idea
#n times (once for every item in the array) I do a binary search? probs on m items. M items = the largest value in the array items