from typing import List, Optional
from listNode import convertArray, convertLinkedList, ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    cur.next, list1 = list1, list1.next
                else:
                    cur.next, list2 = list2, list2.next
                cur = cur.next
            elif list1 is None:
                cur.next = list2
                break
            elif list2 is None:
                cur.next = list1
                break
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
