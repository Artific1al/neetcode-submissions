class Solution:
    def isPalindrome(self, s: str) -> bool:

# CONSTRAINTS        
# a palindrome is a string that is the same forward and back e.g. abcdefedcba
# case insensitive
# ignores non alphanumeric characters
# 1 <= string lenth <= 1000
# made up of ONLY printable ASCII characters


# brute force 
# make a stack
# pop from the stack constantly
# if non alphanumeric -> skip 
# o(N) time + O(n) space we can do better

# two pointers
# start at start & at end
# while pointers a,b (start, end) are not alphanumeric:
# a +=1 / b -=1 
# ensure they don't cross over via -> if a and b would bot skip and cross in the middle
# if a alphanumeric -> if b also alphanumeric -> compare
# if at any point a comparison is not true return False
# 

        # set up pointers
        length = len(s) # in indices
        start = 0
        end = len(s) -1
        

        while start < end: # O(n) times
            # ensure alpha numeric
            if not s[start].isalnum(): # these combined run at most O(n)
                if start + 1 < length:
                    start +=1
            if not s[end].isalnum(): # these combined run at most O(n)
                if end - 1 >= 0:
                    end -=1
            
            # valid comparison
            if s[start].isalnum() and s[end].isalnum():           
                if s[start].lower() == s[end].lower():
                        start +=1
                        end -=1
                else:
                    #return s[end]
                    return False
        return True

# EDGE CASES
# string of length 1 & string of length 2