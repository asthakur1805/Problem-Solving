class Solution:

	def deleteDuplicates(self, head):

		if not head:

			return

		slow, fast = head, head.next

		while fast:

			if slow.val != fast.val:

				slow = slow.next
				slow.val = fast.val

			fast = fast.next

		slow.next = None

		return head