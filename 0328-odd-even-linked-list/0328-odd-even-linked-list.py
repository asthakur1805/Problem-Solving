class Solution:

	def oddEvenList(self, headOdd):

		if not headOdd:

			return

		headEven = headOdd.next

		currOdd, currEven = headOdd, headEven

		while currEven and currEven.next:

			currOdd.next = currOdd.next.next
			currOdd = currOdd.next
			currEven.next = currEven.next.next
			currEven = currEven.next

		currOdd.next = headEven

		return headOdd