class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        while head != None and head.val == val:
            head = head.next
        before,cur = head,head
        while cur:
            if  cur.val != val:
                before = cur
                cur = cur.next
            else:
                cur = cur.next
                before.next = cur
        return head                