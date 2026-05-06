class Stack:
    def __init__(self, length):
        self.array = []
    
    def get(self):
        return self.array.pop()
    
    def add(self, item):
        self.array.append(item)


class Solution:
    def isValid(self, s: str) -> bool:
        
# CONSTRAINTS
# strings only contains chars
# '(', ')', '{', '}', '[', ']'
# 1 <= string len <= 1000

# Valid IF
# -> Every open bracket is closed by the same close bracket
# -> open brackets closed in corrct order
# -> Every close bracket has a corresponding open bracket of same type

# Naive Approach
# make a stack
# for every bracket append the corresponding bracket
# once you hit the first close bracket -> from this point there can be no more open brackets unless
# all brackets are closed

# What makes this challenging to think about? 
# For every bracket -> If open, append a close to the stack
# -> If close'

# for char in string
# if open, append a corresponding close to stack
# if close -> pop from stack and make sure that it is the correct one

        stack = Stack(len(s))
        for char in s:
            if len(s) == 1:
                return False
            if char == '(':
                stack.add(')')
            elif char == '[':
                stack.add(']')
            elif char == '{':
                stack.add('}')
            else:
                if len(stack.array) > 0:
                    if stack.get() is not char:
                        return False
                elif len(stack.array) == 0 and (char == ']' or char == '}' or char == ')'):
                    return False
        if len(stack.array) == 0:
            return True
        else:
            return False