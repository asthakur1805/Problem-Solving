class Solution:

	def calculateLength(self, head):

		result, currNode = 0, head

		while currNode:

			result += 1

			currNode = currNode.next

		return result

	def getIntersectionNode(self, headFirstList, headSecondList):

		firstListLength, secondListLength = self.calculateLength(headFirstList), self.calculateLength(headSecondList)

		currFirstList, currSecondList = headFirstList, headSecondList

		if firstListLength >= secondListLength:

			for _ in range(firstListLength-secondListLength):

				currFirstList = currFirstList.next

		else:

			for _ in range(secondListLength-firstListLength):

				currSecondList = currSecondList.next

		while currFirstList != currSecondList:

			currFirstList = currFirstList.next
			currSecondList = currSecondList.next

		return currFirstList