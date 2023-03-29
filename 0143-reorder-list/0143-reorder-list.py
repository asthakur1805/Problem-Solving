class Solution:

	def reorderList(self, head):
	
		if not head:

			return 

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

		while right.next:

			leftNext, rightNext = left.next, right.next
			left.next, right.next = right, leftNext
			left, right = leftNext, rightNext

		return head