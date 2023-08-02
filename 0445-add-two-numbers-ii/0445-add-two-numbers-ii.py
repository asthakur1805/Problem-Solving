class Solution:

	def addTwoNumbers(self, headFirstList, headSecondList):

		stackFirstList, stackSecondList = [], []

		currFirstList, currSecondList = headFirstList, headSecondList

		while currFirstList:

			stackFirstList.append(currFirstList.val)
			currFirstList = currFirstList.next

		while currSecondList:

			stackSecondList.append(currSecondList.val)
			currSecondList = currSecondList.next

		newHead, carry = None, 0

		while stackFirstList or stackSecondList or carry:

			firstDigit = stackFirstList.pop() if stackFirstList else 0
			secondDigit = stackSecondList.pop() if stackSecondList else 0

			addition = firstDigit + secondDigit + carry

			newHead = ListNode(addition % 10, newHead)

			carry = addition // 10

		return newHead