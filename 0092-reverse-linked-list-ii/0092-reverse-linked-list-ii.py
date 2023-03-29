class Solution:

	def reverseBetween(self, head, start, end):

		if not head:

			return 

		dummy = ListNode(0, head)

		#Phase 1
	
		leftBreak, curr = dummy, head

		for _ in range(start-1):

			leftBreak = leftBreak.next
			curr = curr.next

		#Phase 2
		prev = None

		for _ in range(end-start+1):

			currNext = curr.next
			curr.next = prev
			prev = curr
			curr = currNext

		leftBreak.next.next = curr
		leftBreak.next = prev

		return dummy.next