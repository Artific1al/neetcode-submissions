class Solution:
    def isPalindrome(self, s: str) -> bool:
           sUpper = s.upper()
           sAlpha = ""
        
           for i in range(len(sUpper)):
               if sUpper[i].isalnum():
                   sAlpha += sUpper[i]
            
           for ind in range(len(sAlpha)):
               #edge case - ignore if string is even
               if (len(sAlpha) % 2) !=0 and ind == (len(sAlpha) / 2) + 1:
                   continue
                
               if sAlpha[ind] != sAlpha[len(sAlpha)-1-ind]:
                   return False
           return True


        
        # word = upper(word)
        # newWord = ""

        # for char in s:
        #     if char.isalnum():
        #         newWord = newWord.join(char)
        # stack = []

        # #if even split in half
        # if len(s) % 2 == 0:
        #     if


#Constraints -> only alphanumeric characters

#ignores non 