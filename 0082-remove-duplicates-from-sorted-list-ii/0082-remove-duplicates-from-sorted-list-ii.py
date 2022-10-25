class Solution:

	def deleteDuplicates(self, head):

		dummyNode = ListNode(0, head)

		prevNode, currNode = dummyNode, head

		while currNode and currNode.next:

			if currNode.val != currNode.next.val:

				prevNode = currNode
				currNode = currNode.next

			else:

				while currNode and currNode.next and currNode.val == currNode.next.val:
					
					currNode = currNode.next

				prevNode.next = currNode.next
				currNode = currNode.next


		return dummyNode.next