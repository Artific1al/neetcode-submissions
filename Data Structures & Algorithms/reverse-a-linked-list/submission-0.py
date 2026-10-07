#what.
#I watched the video and understand the theory but what?????

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode):

        if head is None:
            return None

        #end of list -> start a new one
        if head.next == None:
            new = ListNode(val = head.val)
            return new

        else:
            soFar = self.reverseList(head.next)
            original = soFar

            while soFar.next != None:
                 soFar.next = soFar = soFar.next
            
            soFar.next = ListNode(val = head.val)
            return original



        #O(n) time and O(1) space

    #get to end of list
    #once at end of list, create new listNode with previous
    #repeat until at end
        
        