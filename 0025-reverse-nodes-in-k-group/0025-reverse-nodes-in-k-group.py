class Solution:

	def reverseKGroup(self, head, groupLength):

		dummy = ListNode(0, head)

		groupPrev = dummy

		while True:

			groupEnd = self.getGroupEnd(groupPrev, groupLength)

			if not groupEnd:

				break

			prev, curr = groupEnd.next, groupPrev.next

			for _ in range(groupLength):

				nextNode = curr.next
				curr.next = prev
				prev = curr
				curr = nextNode

			groupPrevNext = groupPrev.next

			groupPrev.next = groupEnd
	
			groupPrev = groupPrevNext

		return dummy.next
				
	def getGroupEnd(self, curr, groupLength):

		while curr and groupLength > 0:

			curr = curr.next
			groupLength -= 1

		return curr