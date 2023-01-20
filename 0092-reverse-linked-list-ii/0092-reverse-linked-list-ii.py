class Solution:

	def reverseBetween(self, head, left, right):

		dummy = ListNode(0,head)

		leftBreak, currNode, position = dummy, head, 1

		while position < left:

			leftBreak = leftBreak.next

			currNode = currNode.next

			position += 1

		rightBreak = currNode

		prevNode = None

		while position <= right:

			nextNode = currNode.next
			currNode.next = prevNode
			prevNode = currNode
			currNode = nextNode
			position += 1

		leftBreak.next = prevNode
		rightBreak.next = currNode
			
		return dummy.next