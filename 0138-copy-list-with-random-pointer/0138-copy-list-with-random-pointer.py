class Solution:

	def copyRandomList(self, head):

		if not head:

			return

		curr = head

		while curr:

			newNode = ListNode(curr.val)

			newNode.next = curr.next

			curr.next = newNode

			curr = curr.next.next

		curr = head

		while curr:

			curr.next.random = curr.random.next if curr.random else None

			curr = curr.next.next

		curr = head
		newHead = curr.next

		while curr:

			newNode = curr.next

			curr.next = curr.next.next

			newNode.next = newNode.next.next if newNode.next else None

			curr = curr.next

		return newHead

			