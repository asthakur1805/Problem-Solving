class Solution:

	def detectCycle(self, head):

		currNode = head

		visitedNodes = set()

		while currNode:

			if currNode in visitedNodes:

				return currNode

			visitedNodes.add(currNode)

			currNode = currNode.next

		return 