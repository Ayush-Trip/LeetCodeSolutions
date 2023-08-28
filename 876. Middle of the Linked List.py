# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        temp=head
        while(temp!=None):
            c+=1
            temp=temp.next
        c=c//2
        i=0
        while(i<c):
            head=head.next
            i+=1
        return head
            
            