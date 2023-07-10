class Solution:

	def sortList(self, head):

		if not head:

			return

		return self.mergeSort(head)

	def mergeSort(self, head):

		if not head.next:

			return head

		prev, mid, fast = head, head, head

		while fast and fast.next:

			prev, mid, fast = mid, mid.next, fast.next.next

		prev.next = None

		headLeftList, headRightList = self.mergeSort(head), self.mergeSort(mid)

		dummy = ListNode()

		currLeftList, currRightList, currResultList = headLeftList, headRightList, dummy

		while currLeftList and currRightList:

			if currLeftList.val <= currRightList.val:

				currResultList.next = currLeftList
				currLeftList = currLeftList.next

			else:

				currResultList.next = currRightList
				currRightList = currRightList.next

			currResultList = currResultList.next

		currResultList.next = currLeftList if currLeftList else currRightList

		return dummy.next