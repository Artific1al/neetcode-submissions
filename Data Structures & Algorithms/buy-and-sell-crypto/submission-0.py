class Solution:
    def maxProfit(self, prices: List[int]) -> int:

      
        l = 0
        r = 1
        maxRes = 0

        while r < len(prices):
            
            #case 1 r is bigger
            if prices[r] > prices[l]:
                calc = prices[r] - prices[l]
                if calc > maxRes:
                    maxRes = calc
        
            #case 2 r is smaller than l
            else:
                l = r
                
            r +=1

        return maxRes

#l = 0, r = 1, max = 0
#l = 1, r = 2, max = 4
#l=1, r = 3, max = 5
#l = 1, r = 4, max = 6
#l = 1, r = 5, max = 6 

#[7,1,5,3,6,4]
#l = 0, r = 1, max = 0
#l = 1, r = 2, max = 4

#Constraints
#O(n) time  | O(1) space 
#sell day cannot = buy day

#Brute Force
#O(n^2) for every I check every j after it and if higher than previous pick that combo
#

#lBest = 0, rBest = 1
#max = 0
#l starts at 0, r starts at 1, while l < r,
# if list[r-l] > max, 
# elif r < l:
# l = r, r = r+1
#[0, 7, 1, 9 ,6 ,12, 15, 4]