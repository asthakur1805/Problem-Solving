class Solution:

	def middleNode(self, head):

		curr, length = head, 0

		while curr:

			length += 1

			curr = curr.next

		curr = head

		for _ in range(length // 2):

			curr = curr.next

		return curr