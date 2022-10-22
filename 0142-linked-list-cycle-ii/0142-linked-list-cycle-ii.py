class Solution:

	def detectCycle(self, head):

		slowPointer = fastPointer = head

		while fastPointer and fastPointer.next:

			slowPointer = slowPointer.next
			fastPointer = fastPointer.next.next

			if slowPointer == fastPointer:
				break

		else:
			return

		currPointer = head

		while currPointer != slowPointer:

			currPointer = currPointer.next
			slowPointer = slowPointer.next

		return slowPointer