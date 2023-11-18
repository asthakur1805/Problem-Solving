class Solution:

	def addTwoNumbers(self,headFirstList,headSecondList):

		headFirstList, headSecondList, dummy = self.reverse(headFirstList), self.reverse(headSecondList), ListNode()

		currFirstList, currSecondList, currResultList, carry = headFirstList, headSecondList, dummy, 0

		while currFirstList or currSecondList or carry:

			firstDigit = currFirstList.val if currFirstList else 0
		
			secondDigit = currSecondList.val if currSecondList else 0

			addition = firstDigit + secondDigit + carry

			currResultList.next = ListNode(addition%10)

			carry = addition // 10

			currFirstList = currFirstList.next if currFirstList else None

			currSecondList = currSecondList.next if currSecondList else None

			currResultList = currResultList.next

		return self.reverse(dummy.next)

	def reverse(self,head):

		prev, curr = None, head

		while curr:

			currNext = curr.next

			curr.next = prev
	
			prev = curr

			curr = currNext

		return prev