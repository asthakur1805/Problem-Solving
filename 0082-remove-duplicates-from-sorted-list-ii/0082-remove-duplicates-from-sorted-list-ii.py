class Solution:

	def deleteDuplicates(self, head):

		if not head:
			
			return

		dummyNode = ListNode()

		dummyNode.next = head

		prevNode, currNode = dummyNode, head

		while currNode and currNode.next:

			if currNode.val != currNode.next.val:

				prevNode = prevNode.next
				currNode = currNode.next

			else:

				while currNode.next and currNode.val == currNode.next.val:

					currNode = currNode.next

				currNode = currNode.next

				prevNode.next = currNode

		return dummyNode.next