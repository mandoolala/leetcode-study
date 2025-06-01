from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(None)
        merge_list = dummy_head

        while list1 and list2:
            if list1.val < list2.val:
                merge_list.next = list1
                list1 = list1.next
            else:
                merge_list.next = list2
                list2 = list2.next
            merge_list = merge_list.next
        merge_list.next = list1 or list2
        return dummy_head.next


