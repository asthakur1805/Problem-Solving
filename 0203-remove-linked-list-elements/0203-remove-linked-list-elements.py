class Solution:

	def removeElements(self, head, inputVal):

		dummyNode = ListNode(0, head)

		currNode = dummyNode

		while currNode.next:

			if currNode.next.val == inputVal:

				currNode.next = currNode.next.next

			else:

				currNode = currNode.next

		return dummyNode.next