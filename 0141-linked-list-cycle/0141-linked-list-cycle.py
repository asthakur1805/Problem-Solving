class Solution:

	def hasCycle(self, head):

		slowPointer = fastPointer = head

		while fastPointer and fastPointer.next:

			slowPointer = slowPointer.next
			fastPointer = fastPointer.next.next

			if slowPointer == fastPointer:

				return True

		return False