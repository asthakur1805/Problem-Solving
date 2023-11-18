class Solution:

	def addTwoNumbers(self,headFirstList,headSecondList):

		stackFirstList, stackSecondList = self.helper(headFirstList), self.helper(headSecondList)

		headResultList, carry = None, 0

		while stackFirstList or stackSecondList or carry:

			firstDigit = stackFirstList.pop() if stackFirstList else 0

			secondDigit = stackSecondList.pop() if stackSecondList else 0

			addition = firstDigit + secondDigit + carry

			headResultList = ListNode(addition%10,headResultList)

			carry = addition // 10

		return headResultList

	def helper(self,head):

		curr, stack = head, []

		while curr:

			stack.append(curr.val)

			curr = curr.next

		return stack