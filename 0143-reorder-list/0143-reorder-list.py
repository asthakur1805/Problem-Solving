class Solution:

	def reorderList(self, head):

		if not head:

			return

		slowPointer, fastPointer = head, head

		while fastPointer and fastPointer.next:

			slowPointer = slowPointer.next
			fastPointer = fastPointer.next.next

		prevPointer = None

		while slowPointer:

			nextNode = slowPointer.next
			slowPointer.next = prevPointer
			prevPointer = slowPointer
			slowPointer = nextNode

		leftPointer, rightPointer = head, prevPointer

		while rightPointer.next:

			nextLeft, nextRight = leftPointer.next, rightPointer.next
			leftPointer.next, rightPointer.next = rightPointer, nextLeft
			leftPointer, rightPointer = nextLeft, nextRight

		return head