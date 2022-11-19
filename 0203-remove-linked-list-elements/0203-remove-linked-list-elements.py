class Solution:

	def removeElements(self, head, inputVal):

		dummyNode = ListNode(0, head)

		prevNode, currNode = dummyNode, head

		while currNode:

			if currNode.val == inputVal:

				prevNode.next = currNode.next

			else:

				prevNode = prevNode.next

			currNode = currNode.next

		return dummyNode.next