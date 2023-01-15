class Solution:

	def getIntersectionNode(self, headFirstList, headSecondList):

		currFirstList, currSecondList = headFirstList, headSecondList

		while currFirstList != currSecondList:

			currFirstList = currFirstList.next if currFirstList else headSecondList

			currSecondList = currSecondList.next if currSecondList else headFirstList

		return currFirstList