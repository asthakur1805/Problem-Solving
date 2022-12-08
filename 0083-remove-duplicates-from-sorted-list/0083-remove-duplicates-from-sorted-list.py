class Solution:

	def deleteDuplicates(self, head):

		if not head:

			return

		slowPointer, fastPointer = head, head.next

		while fastPointer:

			if slowPointer.val != fastPointer.val:

				slowPointer = slowPointer.next

				slowPointer.val = fastPointer.val

			fastPointer = fastPointer.next

		slowPointer.next = None

		return head