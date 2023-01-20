class Solution:

	def reverseList(self, head):

		prevPointer = None

		while head:

			nextNode = head.next

			head.next = prevPointer

			prevPointer = head

			head = nextNode

		return prevPointer