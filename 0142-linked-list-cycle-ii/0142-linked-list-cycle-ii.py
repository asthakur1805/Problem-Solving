class Solution:

	def detectCycle(self, head):

		visitedNodes = set()

		curr = head

		while curr:

			if curr in visitedNodes:

				return curr

			visitedNodes.add(curr)

			curr = curr.next

		return None