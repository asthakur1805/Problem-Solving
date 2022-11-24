class Solution:

	def hasCycle(self, head):

		visitedNodes = set()

		currNode = head

		while currNode:

			if currNode in visitedNodes:

				return True

			visitedNodes.add(currNode)

			currNode = currNode.next

		return False