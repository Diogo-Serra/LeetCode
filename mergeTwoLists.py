from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None) -> None:
        self.val: int = val
        self.next: ListNode = next

    def __str__(self) -> str:
        return f"Value: {self.val}"


class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode],
    ) -> Optional[ListNode]:
        unpack1: list[int] = []
        unpack2: list[int] = []
        if list1:
            unpack1 = unpack(list1)
        if list2:
            unpack2 = unpack(list2)
        if not list1 and not list2:
            return None
        unpack1.extend(unpack2)
        sorted_unpacked = sorted(unpack1)
        head = create_linked_list(sorted_unpacked)
        return head


def create_linked_list(_list: list[int]) -> ListNode:

    if not _list:
        return None

    head = ListNode(_list[0])
    curr = head

    for val in _list[1:]:
        curr.next = ListNode(val)
        curr = curr.next

    return head


def unpack(header: ListNode) -> list[int]:

    curr: ListNode = header
    unpacked: list[int] = []
    while curr:
        unpacked.append(curr.val)
        curr = curr.next
    return unpacked
