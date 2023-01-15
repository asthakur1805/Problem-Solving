class Solution:

	def getIntersectionNode(self, headFirstList, headSecondList):

		visitedNodes = set()

		currFirstList = headFirstList	

		while currFirstList:

			visitedNodes.add(currFirstList)

			currFirstList = currFirstList.next

		currSecondList = headSecondList

		while currSecondList:

			if currSecondList in visitedNodes:

				return currSecondList

			currSecondList = currSecondList.next

		return