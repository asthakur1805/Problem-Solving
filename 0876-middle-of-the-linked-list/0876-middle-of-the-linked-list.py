class Solution:

	def middleNode(self, head):

		if not head:

			return

		slowPointer = fastPointer = head 

		while fastPointer and fastPointer.next:	

			slowPointer = slowPointer.next

			fastPointer = fastPointer.next.next

		return slowPointer