class Solution:

	def copyRandomList(self, head):

		if not head:

			return

		curr = head

		while curr:

			copy = ListNode(curr.val)

			copy.next = curr.next

			curr.next = copy

			curr = curr.next.next

		curr = head

		while curr:

			curr.next.random = curr.random.next if curr.random else None

			curr = curr.next.next

		curr, resultHead = head, head.next

		while curr:

			copy = curr.next

			curr.next = curr.next.next
			copy.next = copy.next.next if copy.next else None

			curr = curr.next

		return resultHead