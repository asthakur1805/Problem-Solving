class Solution:

	def partition(self,head,inputVal):

		leftDummy, rightDummy = ListNode(), ListNode()

		currLeft, currRight, curr = leftDummy, rightDummy, head

		while curr:

			if curr.val < inputVal:

				currLeft.next = curr
				currLeft = currLeft.next
			
			else:
				
				currRight.next = curr
				currRight = currRight.next

			curr = curr.next

		currLeft.next, currRight.next = rightDummy.next, None

		return leftDummy.next