#two pointers in link list in gfg
#876
'''# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
            sp=head
            fp=head
            while fp and fp.next:
                sp=sp.next
                fp=fp.next.next
            return sp
        '''

#141
'''# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        f=s=head
        while f and f.next:
            f=f.next.next
            s=s.next
            if f==s:
                return True
        return False'''

#202
