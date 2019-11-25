class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        start = ListNode(None)
        new_node = start
        while l1 and l2:
            if l1.val <= l2.val:
                new_node.next = l1
                l1 = l1.next
            else:
                new_node.next = l2
                l2 = l2.next
            new_node = new_node.next
        if l1:
            new_node.next = l1
        else:
            new_node.next = l2
        return start.next