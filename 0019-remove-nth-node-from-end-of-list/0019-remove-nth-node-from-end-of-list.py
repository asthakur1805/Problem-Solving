class Solution:

	def removeNthFromEnd(self, head, N):

		dummyNode = ListNode(0, head)

		currNode = head

		for _ in range(N):

			currNode = currNode.next

		prevNode = dummyNode

		while currNode:

			currNode = currNode.next
			prevNode = prevNode.next

		prevNode.next = prevNode.next.next

		return dummyNode.next