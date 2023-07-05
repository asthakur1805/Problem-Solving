class Solution:

	def insertionSortList(self, head):

		dummy = ListNode(0,head)

		curr, prev = head.next, head

		while curr:

			if curr.val >= prev.val:

				curr, prev = curr.next, prev.next
				continue

			iter = dummy

			while iter.next.val <= curr.val:

				iter = iter.next

			prev.next = curr.next
			curr.next = iter.next
			iter.next = curr
			curr = prev.next

		return dummy.next