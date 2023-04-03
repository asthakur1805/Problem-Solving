class Solution:

	def removeElements(self, head, inputVal):

		dummy = ListNode(0, head)

		prev, curr = dummy, head

		while curr:

			if curr.val == inputVal:

				prev.next = curr.next

			else:

				prev = prev.next

			curr = curr.next

		return dummy.next