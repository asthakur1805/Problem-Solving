class Solution:

	def isPalindrome(self, head):

		slow, fast = head, head

		while fast and fast.next:

			slow = slow.next

			fast = fast.next.next

		prev = None

		while slow:

			nextNode = slow.next

			slow.next = prev

			prev = slow

			slow = nextNode

		leftPointer, rightPointer = head, prev

		while rightPointer:

			if leftPointer.val != rightPointer.val:

				return False

			leftPointer = leftPointer.next
			rightPointer = rightPointer.next

		return True