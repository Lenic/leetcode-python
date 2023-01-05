from typing import List, Optional
from listNode import convertArray, convertLinkedList, ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = dummy = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                res.next = list1
                list1 = list1.next
            else:
                res.next = list2
                list2 = list2.next
            res = res.next
        res.next = list1 if list1 is not None else list2
        while res.next:
            res = res.next
        res.next = None
        return dummy.next


def polyfill(l1: List[int], l2: List[int]):
    res = Solution().mergeTwoLists(convertArray(l1), convertArray(l2))
    print(convertLinkedList(res))


# [0]
polyfill(l1=[], l2=[0])

# []
polyfill(l1=[], l2=[])

# [1,1,2,3,4,4]
polyfill(l1=[1, 2, 4], l2=[1, 3, 4])

# [1,1,2,3,4,4,5]
polyfill(l1=[1, 2, 4], l2=[1, 3, 4, 5])
