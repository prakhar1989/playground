class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        dummy = ListNode(-1) # used as a starting pointer
        tmp = dummy
        while l1 is not None or l2 is not None:
            val = carry
            if l1 is not None:
                val += l1.val
                l1 = l1.next
            if l2 is not None:
                val += l2.val
                l2 = l2.next
            carry, val = val / 10, val % 10
            tmp.next = ListNode(val)
            tmp = tmp.next
        if carry == 1:
            tmp.next = ListNode(1)
        return dummy.next
