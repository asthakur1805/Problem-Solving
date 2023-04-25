class Solution:

	def sortedListToBST(self, head):

		if not head:

			return None

		if not head.next:

			return TreeNode(head.val)

		mid = self.middleNode(head)

		root = TreeNode(mid.val)

		prev = head

		while prev.next != mid:

			prev = prev.next

		prev.next = None

		root.left, root.right = self.sortedListToBST(head), self.sortedListToBST(mid.next)

		return root


	def middleNode(self, head):

		slow, fast = head, head

		while fast and fast.next:

			slow, fast = slow.next, fast.next.next

		return slow