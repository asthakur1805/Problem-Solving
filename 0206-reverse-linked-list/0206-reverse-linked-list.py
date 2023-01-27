class Solution:

	def reverseList(self, head):

		curr, prev = head, None

		while curr:

			nextNode = curr.next

			curr.next = prev

			prev = curr

			curr = nextNode

		return prev