class Solution:

	def sortedListToBST(self, head):

		if not head:

			return

		mid = self.middleNode(head)

		root = TreeNode(mid.val)

		if mid == head:

			return root

		root.left = self.sortedListToBST(head)

		root.right = self.sortedListToBST(mid.next)

		return root

		
	def middleNode(self, head):

		prev, slow, fast = head, head, head

		while fast and fast.next:

			prev = slow
			slow = slow.next
			fast = fast.next.next

		prev.next = None

		return slow