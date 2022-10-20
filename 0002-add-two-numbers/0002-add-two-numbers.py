class Solution:

	def addTwoNumbers(self, headFirstList, headSecondList):

		dummyNode = ListNode()

		currFirstList, currSecondList, currResultList = headFirstList, headSecondList, dummyNode

		carry  = 0

		while currFirstList or currSecondList or carry:

			digitFirstList = currFirstList.val if currFirstList else 0
			digitSecondList = currSecondList.val if currSecondList else 0

			addition = digitFirstList + digitSecondList + carry

			currResultList.next = ListNode(addition % 10)

			carry = addition // 10

			currFirstList = currFirstList.next if currFirstList else None
			currSecondList = currSecondList.next if currSecondList else None
			currResultList = currResultList.next

		return dummyNode.next