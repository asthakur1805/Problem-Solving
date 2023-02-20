class Solution:

	def reverseBetween(self, head, left, right):

		dummy = ListNode(0, head)

		leftPrev, curr = dummy, head

		for _ in range(left-1):

			leftPrev = leftPrev.next
			curr = curr.next

		prev = None

		for _ in range(right-left+1):

			nextNode = curr.next
			curr.next = prev
			prev = curr
			curr = nextNode

		leftPrev.next.next = curr
		leftPrev.next = prev

		return dummy.next
		