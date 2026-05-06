class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operands = ['+', '-', '*', '/']

        for token in tokens:
            #operand found -> perform evaluation
            if token in operands:
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                stack.append(self.chrToOperand(val1, val2, token))
            
            else:
                stack.append(token)
        
        return int(stack.pop())

    
    def chrToOperand(self, val1: int, val2: int, operand: str):
        #operand can only be + - / *
        if operand == "+":
            return val1 + val2
        elif operand == "-":
            return val1 - val2
        elif operand == "*":
            return val1 * val2
        elif operand == "/":
            return int(val1 / val2)
        else:
            #raise error
            return math.inf 
                    


   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    #     stack = []
    #     val1 = 0
    #     val2 = 0
    #     currentToken = ""
    #     operands = ['+', '-', '*', '/']

    #     #append tokens in reverse order
    #     for token in range(len(tokens)-1, -1, -1):
    #         stack.append(tokens[token])
        
    #     while stack:
    #         currentToken = stack.pop()

    #         if len(stack) == 0 and currentToken not in operands:
    #             return int(currentToken)
    #         #get current
        
    #         #case 2: perform operation and add to stack
    #         if currentToken in operands:
    #             stack.append(str(self.chrToOperand(val1, val2, currentToken)))

    #         #case 1: get two nums and 
    #         else:
    #             val1 = int(currentToken)
    #             val2 = int(stack.pop())
        
    #     return val2 
        

   
#Constraints
#O(n) time and space
#between 1-1000 tokens
#tokens are + - * / or the string of a num in range [-100, 100]
#will always start with a num and end with an operand
#all operands take exactly two nums, +


#Reverse polish notation?
#Postfix Notation = operator operator operand == 3 4 + = 7 

#Brute force -> iterate through list and 
#have 3 counters, val1, val2, current
#every time you get two values store them and once you find a operand do val operand val2 
#then append result to stack and move two indexes to the left

#Assuming only 3 4 + is valid
#Idea -> from end of string append everything to stack O(n)
#Have two mutable vals
#then pop from stack one at a time and there are 2 valid cases:
#case 1: num -> add to current vals
#case 2: operand -> only ever takes two nums so do operation then append back to top of stack
#happens at most n/2 times = O(n) still


#Ok so you can have an unlimited number of them in a row
#

