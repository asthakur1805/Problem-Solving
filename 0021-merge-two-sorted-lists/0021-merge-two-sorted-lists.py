class Solution:

	def mergeTwoLists(self, headFirstList, headSecondList):

		dummyNode = ListNode()

		currFirstList, currSecondList, currResultList = headFirstList, headSecondList, dummyNode

		while currFirstList and currSecondList:

			if currFirstList.val < currSecondList.val:

				currResultList.next = currFirstList
				currFirstList = currFirstList.next
				
			else:

				currResultList.next = currSecondList
				currSecondList = currSecondList.next

			currResultList = currResultList.next

		currResultList.next = currFirstList if currFirstList else currSecondList

		return dummyNode.next

		

			
	
		