class Solution:

	def reverseBetween(self, head, left, right):

		dummyNode = ListNode(0,head)

		leftBreak, currNode = dummyNode, head

		for _ in range(left-1):

			currNode = currNode.next
			leftBreak = leftBreak.next

		prevNode = None

		for _ in range(right-left+1):

			nextNode = currNode.next
			currNode.next = prevNode
			prevNode = currNode
			currNode = nextNode

		leftBreak.next.next = currNode
		leftBreak.next = prevNode

		return dummyNode.next
		