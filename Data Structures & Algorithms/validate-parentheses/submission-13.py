class Solution:
    def isValid(self, s: str) -> bool:
        
    
        stack = []

        #len 1 will always be false
        if len(s) == 1:
            return False

        for char in s:
            
            #if open char, add to stack
            if char == '(':
                stack.append(')')
            elif char == '[':
                stack.append(']')
            elif char == '{':
                stack.append('}')

            #if close char, check it = stack.pop
            elif char == ')':
                #if stack empty then invalid close bracket | if stack not empty
                if len(stack) == 0 or stack.pop() != char:
                    return False
            elif char == ']':
                if len(stack) == 0 or  stack.pop() != char:
                    return False
            elif char == '}':
                if len(stack) == 0 or stack.pop() != char:
                    return False
            
            #no other cases
        
        #if stack len >0 then we have un paired open brackets
        return len(stack) == 0



#Constraints
#chars are only (, ), {, }, [ and ]
#O(n) time and space 
#string len between 1 and 1000

#Brute Force
#Create a stack
#every time you see an open, add to top of stack corresponding close
#if you ever run into a mismatch or stack is not empty - false

#Edge cases
#what if there is empty string ->

#()
#