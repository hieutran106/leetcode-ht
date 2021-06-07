from utils.my_list import ListNode
from utils.my_tree import TreeNode


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        return self.helper(head)

    def helper(self, start, end=None) -> TreeNode:
        if (start is None) or (start == end):
            return None

        fast = start
        slow = start

        while fast.next != end or fast.next.next != end:
            fast = fast.next.next
            slow = fast.next

        root = TreeNode(slow.val)
        root.left = self.helper(start, slow)
        root.right = self.helper(slow.next, end)
        return root


class Solution2:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        data = []
        while head is not None:
            data.append(head.val)
            head = head.next

        root = self.build_tree(data)
        return root

    def build_tree(self, data):
        if len(data) == 0:
            return None
        middle = len(data) // 2
        root = TreeNode(data[middle])
        root.left = self.build_tree(data[:middle])
        root.right = self.build_tree(data[middle + 1:])
        return root
