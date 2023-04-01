class Solution:

	def isPalindrome(self, head):

		slow, fast = head, head

		while fast and fast.next:

			slow = slow.next
			fast = fast.next.next

		prev = None

		while slow:

			slowNext = slow.next
			slow.next = prev
			prev = slow
			slow = slowNext

		left, right = head, prev

		while right:

			if left.val != right.val:

				return False

			left, right = left.next, right.next

		return True