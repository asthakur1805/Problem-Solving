class Solution:

	def swapPairs(self, head):

		dummyNode = ListNode(0,head)

		prevNode, firstNode = dummyNode, head

		while firstNode and firstNode.next:

			secondNode = firstNode.next

			firstNode.next = secondNode.next
			secondNode.next = firstNode
			prevNode.next = secondNode

			prevNode = firstNode
			firstNode = firstNode.next

		return dummyNode.next