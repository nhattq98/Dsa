from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"


class LinkedList:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


def test():
    head = ListNode(0)
    head.next = ListNode(1)
    head.next = ListNode(2)
    head.next = ListNode(3)

    linkedListTest = LinkedList()

    result = linkedListTest.hasCycle(head=head)
    print(result)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test()
