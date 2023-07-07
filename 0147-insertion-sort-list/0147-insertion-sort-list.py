class Solution:

	def insertionSortList(self, head):

		if not head:

			return

		dummy = ListNode(0, head)

		prev, curr = head, head.next

		while curr:

			if prev.val <= curr.val:

				prev, curr = prev.next, curr.next

				continue

			temp = dummy

			while temp.next.val <= curr.val:

				temp = temp.next

			prev.next = curr.next
			curr.next = temp.next
			temp.next = curr
			curr = prev.next

		return dummy.next