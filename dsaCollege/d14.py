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

'''class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()  # To detect cycles

        while n != 1 and n not in seen:
            seen.add(n)
            t = n
            s = 0
            while t > 0:
                d = t % 10          
                s += d**2           
                t //= 10            
            n = s                   
        return n == 1'''

#19

'''# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p=q=head
        for i in range(n):
            q=q.next
        if q==None:
            return head.next
        while q.next!=None:
            p=p.next
            q=q.next
        if p.next:
            p.next=p.next.next
        return head'''