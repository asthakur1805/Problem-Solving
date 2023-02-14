class Solution:

	def reverseList(self, head):

		if not head:

			return

		prev,curr = None, head

		while curr:

			nextNode = curr.next

			curr.next = prev

			prev = curr

			curr = nextNode

		return prev