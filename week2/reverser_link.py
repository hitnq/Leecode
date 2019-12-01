class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pCur = head
        pRev = None
        while pCur:
            pTemp = pCur
            pCur = pCur.next
            pTemp.next = pRev
            pRev = pTemp
        return pRev