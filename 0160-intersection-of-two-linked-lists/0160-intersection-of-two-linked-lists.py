
# Difference in list lengths
class Solution:

	def calculateListLength(self, head):
	
		currPointer, resultLength = head, 0

		while currPointer:

			resultLength += 1

			currPointer = currPointer.next

		return resultLength

	def getIntersectionNode(self, headFirstList, headSecondList):
	
		firstListLength, secondListLength = self.calculateListLength(headFirstList), self.calculateListLength(headSecondList)
	
		currFirstList, currSecondList = headFirstList, headSecondList
	
		if firstListLength > secondListLength:
			
			for _ in range(firstListLength-secondListLength):
	
				currFirstList = currFirstList.next
			
		else:
	
			for _ in range(secondListLength-firstListLength):
	
				currSecondList = currSecondList.next
	
		while currFirstList != currSecondList:
	
			currFirstList = currFirstList.next
			currSecondList = currSecondList.next
	
		return currFirstList
