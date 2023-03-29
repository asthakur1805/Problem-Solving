class Solution:

	def rotateRight(self, head, numRotations):

		if not head:

			return

		tail, listLength = head, 1

		while tail.next:

			listLength += 1
			tail = tail.next

		leftBreak, numRotations = head, numRotations % listLength

		for _ in range(listLength - numRotations - 1):

			leftBreak = leftBreak.next

		tail.next = head
		head = leftBreak.next
		leftBreak.next = None

		return head
