"""
Given a non-empty, singly linked list with head node head, return a middle node of linked list.
If there are two middle nodes, return the second middle node.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def middleNode(self, head: ListNode) -> ListNode:
        one= head
        two= head
        count=1
        while(two):
            if(count%2==0):
                one=one.next
            two=two.next
            count += 1 
        return one

