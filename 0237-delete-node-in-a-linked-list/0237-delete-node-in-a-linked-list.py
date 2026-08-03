# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        # if node is None or node.next is None:
        #     return None
        # curr=node
        # while curr.next.next is not None:
        #     curr=curr.next
        # curr.next=None
        # return node        
        