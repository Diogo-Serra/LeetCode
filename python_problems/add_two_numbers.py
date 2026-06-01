#!/usr/bin/env python3
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        pass


if __name__ == '__main__':

    solution = Solution()
    solution_list = solution.addTwoNumbers([1, 2, 3], [2, 2, 2])
