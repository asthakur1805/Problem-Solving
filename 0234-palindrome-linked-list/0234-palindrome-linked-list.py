class Solution:

	def isPalindrome(self, head):

		slowPointer, fastPointer = head, head

		while fastPointer and fastPointer.next:

			fastPointer = fastPointer.next.next

			slowPointer = slowPointer.next

		prevNode = None

		while slowPointer:

			nextNode = slowPointer.next

			slowPointer.next = prevNode

			prevNode = slowPointer

			slowPointer = nextNode

		leftPointer, rightPointer = head, prevNode

		while rightPointer:

			if leftPointer.val != rightPointer.val:

				return False

			leftPointer = leftPointer.next

			rightPointer = rightPointer.next

		return True