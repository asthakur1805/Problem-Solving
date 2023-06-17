class Solution:

	def partition(self, head, midValue):

		leftDummy, rightDummy = ListNode(), ListNode()

		leftTail, rightTail, curr = leftDummy, rightDummy, head

		while curr:

			if curr.val < midValue:

				leftTail.next = curr
				leftTail = leftTail.next

			else:

				rightTail.next = curr
				rightTail = rightTail.next

			curr = curr.next

		leftTail.next = rightDummy.next
		rightTail.next = None

		return leftDummy.next