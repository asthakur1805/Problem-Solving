class Solution:

	def reverseList(self, head):

		curr, prev = head, None

		while curr:

			currNext = curr.next
			curr.next = prev
			prev = curr
			curr = currNext

		return prev
