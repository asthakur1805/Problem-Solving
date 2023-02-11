class Solution:

	def removeElements(self, head, number):

		if not head:

			return

		dummy = ListNode(0, head)

		prev, curr = dummy, head

		while curr:

			if curr.val != number:

				prev = prev.next

			else:

				prev.next = curr.next

			curr = curr.next

		return dummy.next