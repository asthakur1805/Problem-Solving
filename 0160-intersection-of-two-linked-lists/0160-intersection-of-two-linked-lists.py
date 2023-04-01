class Solution:

	def getIntersectionNode(self, headFirstList, headSecondList):

		firstListLength, secondListLength = self.calculateLength(headFirstList), self.calculateLength(headSecondList)

		currFirstList, currSecondList = headFirstList, headSecondList

		if firstListLength > secondListLength:

			for _ in range(firstListLength-secondListLength):

				currFirstList = currFirstList.next

		else:

			for _ in range(secondListLength-firstListLength):

				currSecondList = currSecondList.next

		while currFirstList != currSecondList:

			currFirstList, currSecondList = currFirstList.next, currSecondList.next

		return currFirstList

		

	def calculateLength(self, head):

		curr, resultLength = head, 0

		while curr:

			resultLength += 1
	
			curr = curr.next

		return resultLength

		