
class Solution:

	def hasCycle(self, head):

		currNode, visitedNodes = head, set()

		while currNode:

			if currNode in visitedNodes:

				return True

			visitedNodes.add(currNode)

			currNode = currNode.next

		return False