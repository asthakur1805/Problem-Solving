class Solution:

	def addTwoNumbers(self, headFirstList, headSecondList):

		firstListLength, secondListLength = self.getLength(headFirstList), self.getLength(headSecondList)

		if firstListLength < secondListLength:

			headFirstList, headSecondList = headSecondList, headFirstList
			firstListLength, secondListLength = secondListLength, firstListLength

		currFirstList, currSecondList, currResultList = headFirstList, headSecondList, None

		for _ in range(firstListLength-secondListLength):

			currResultList = ListNode(currFirstList.val,currResultList)
			currFirstList = currFirstList.next

		for _ in range(secondListLength):

			currResultList = ListNode(currFirstList.val+currSecondList.val, currResultList)
			currFirstList, currSecondList = currFirstList.next, currSecondList.next

		prev, carry = None, 0

		while currResultList:

			currResultList.val += carry
			
			carry = currResultList.val // 10

			currResultList.val %= 10

			nextNode = currResultList.next
			currResultList.next = prev
			prev = currResultList
			currResultList = nextNode

		if carry:

			prev = ListNode(1,prev)

		return prev
			

	def getLength(self, head):

		curr, result = head, 0

		while curr:

			result += 1
			curr = curr.next

		return result