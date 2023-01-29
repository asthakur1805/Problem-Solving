class Solution:

	def rotateRight(self, head, numRotations):

		if not head:

			return

		tail, numsLength = head, 1

		while tail.next:

			numsLength += 1

			tail = tail.next

		leftBreak, numRotations = head, numRotations % numsLength

		for _ in range(numsLength-numRotations-1):

			leftBreak = leftBreak.next

		tail.next = head

		head = leftBreak.next

		leftBreak.next = None

		return head

		

		