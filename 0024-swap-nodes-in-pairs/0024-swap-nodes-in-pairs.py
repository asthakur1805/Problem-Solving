class Solution:

	def swapPairs(self, head):

		if not head or not head.next:
			return head

		firstNode, secondNode = head, head.next

		dummyNode = ListNode()

		prevNode = dummyNode

		while firstNode and secondNode:

			firstNode.next = secondNode.next
			secondNode.next = firstNode
			prevNode.next = secondNode
			
			prevNode = firstNode
			firstNode = firstNode.next

			if firstNode:
				secondNode = firstNode.next

		return dummyNode.next

	