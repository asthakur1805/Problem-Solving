class Solution:

	def getIntersectionNode(self, headFirstList, headSecondList):

		curr, visitedNodes = headFirstList, set()

		while curr:

			visitedNodes.add(curr)

			curr = curr.next

		curr = headSecondList

		while curr:

			if curr in visitedNodes:

				return curr

			curr = curr.next

		return None