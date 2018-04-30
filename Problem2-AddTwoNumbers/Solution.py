# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """


        if l1==None:
            l3 = ListNode(l2.val)
            l2 = l2.next
        elif l2==None:
            l3 = ListNode(l1.val)
            l1 = l1.next
        else:
            val = l1.val+l2.val
            if val>9:
                ones = val%10
                tens = val//10
                l3 = ListNode(ones)
                c=tens
            else:
                c=0
                l3 = ListNode(val)
            l1 = l1.next
            l2 = l2.next

        current = l3
        while l1!=None or l2!=None:
            if l1==None:
                val = l2.val+c
                l2 = l2.next

            elif l2==None:
                val = l1.val+c
                l1 = l1.next


            else:
                val = l1.val+l2.val+c
                l1 = l1.next
                l2 = l2.next

            if val>9:
                ones = val%10
                tens = val//10
                newNode = ListNode(ones)
                current.next = newNode
                current = current.next
                c=tens
            else:
                c=0
                current.next = ListNode(val)
                current = current.next
        if c!=0:
            newNode = ListNode(c)
            current.next = newNode
        return l3
## Time Complexity is O(m+n) where m is number of elements of list1 and n is number of elements of list2
