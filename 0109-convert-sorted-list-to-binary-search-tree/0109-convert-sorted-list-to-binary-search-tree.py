class Solution:

	def sortedListToBST(self, head):

		if not head:
			return

		mid = self.findMidNode(head)

		root = TreeNode(mid.val)

		if mid == head:
			return root

		root.left = self.sortedListToBST(head)
		root.right = self.sortedListToBST(mid.next)
			
		return root
	
	def findMidNode(self, head):

		prevPointer = slowPointer = fastPointer = head

		while fastPointer and fastPointer.next:

			prevPointer = slowPointer
			slowPointer = slowPointer.next
			fastPointer = fastPointer.next.next

		prevPointer.next = None

		return slowPointer

	