class Solution:

	def deleteDuplicates(self, head):

		dummy = ListNode(0, head)

		prev, curr = dummy, head

		while curr and curr.next:

			if curr.val != curr.next.val:
	
				prev = prev.next
				curr = curr.next

			else:

				while curr and curr.next and curr.val == curr.next.val:

					curr = curr.next

				prev.next = curr.next
				curr = curr.next

		return dummy.next
				