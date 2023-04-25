class Solution:

	def removeNthFromEnd(self, head, N):

		curr = head

		for _ in range(N):

			curr = curr.next

		dummy = ListNode(0, head)

		prev = dummy

		while curr:

			prev = prev.next
			curr = curr.next

		prev.next = prev.next.next

		return dummy.next
		