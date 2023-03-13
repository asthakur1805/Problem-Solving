class Solution:

	def reorderList(self, head):

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

		left, right = head, prev

		while right.next:

			leftNext, rightNext = left.next, right.next
			left.next = right
			right.next = leftNext
			left = leftNext
			right = rightNext

		return head
		
		