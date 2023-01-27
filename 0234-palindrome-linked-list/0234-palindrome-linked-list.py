class Solution:

	def isPalindrome(self, head):

		slowPointer, fastPointer = head, head

		while fastPointer and fastPointer.next:

			slowPointer = slowPointer.next
			fastPointer = fastPointer.next.next

		prev = None

		while slowPointer:

			nextNode = slowPointer.next
			slowPointer.next = prev
			prev = slowPointer
			slowPointer = nextNode

		leftPointer, rightPointer = head, prev

		while rightPointer:

			if leftPointer.val != rightPointer.val:

				return False

			leftPointer = leftPointer.next
			rightPointer = rightPointer.next

		return True
	
