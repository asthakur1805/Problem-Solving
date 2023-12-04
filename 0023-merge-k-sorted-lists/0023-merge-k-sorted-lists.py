class Solution:

	def mergeKLists(self,lists):

		while len(lists) > 1:

			mergedLists = []
	
			for index in range(0,len(lists),2):

				headFirstList = lists[index]
				headSecondList = lists[index+1] if index+1<len(lists) else None

				mergedLists.append(self.mergeTwoLists(headFirstList,headSecondList))

			lists = mergedLists

		return lists[0] if lists else None

	def mergeTwoLists(self,headFirstList,headSecondList):

		dummy = ListNode()

		currFirstList, currSecondList, currResultList = headFirstList, headSecondList, dummy

		while currFirstList and currSecondList:

			if currFirstList.val <= currSecondList.val:

				currResultList.next = currFirstList
				currFirstList = currFirstList.next
	
			else:

				currResultList.next = currSecondList
				currSecondList = currSecondList.next

			currResultList = currResultList.next

		currResultList.next = currFirstList if currFirstList else currSecondList
	
		return dummy.next

		