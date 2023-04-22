class Solution:

	def addTwoNumbers(self, headFirstList, headSecondList):

		dummyNode = ListNode()

		currFirstList, currSecondList, currResultList, carry = headFirstList, headSecondList, dummyNode, 0

		while currFirstList or currSecondList or carry:

			firstVal = currFirstList.val if currFirstList else 0
			secondVal = currSecondList.val if currSecondList else 0

			addition = firstVal + secondVal + carry

			currResultList.next = ListNode(addition % 10)
			
			carry = addition // 10

			currFirstList = currFirstList.next if currFirstList else None
			currSecondList = currSecondList.next if currSecondList else None
			currResultList = currResultList.next

		return dummyNode.next

			