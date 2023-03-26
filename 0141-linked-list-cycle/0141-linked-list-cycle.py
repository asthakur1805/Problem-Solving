class Solution:

	def hasCycle(self, head):

		visitedNodes = set()

		curr = head

		while curr:

			if curr in visitedNodes:

				return True

			visitedNodes.add(curr)

			curr = curr.next

		return False