from heapq import heappush, heappop

class Solution:

	ListNode.__lt__ = lambda firstNode,secondNode: firstNode.val < secondNode.val

	def mergeKLists(self,lists):

		minHeap = []

		for headCurrList in lists:

			if headCurrList:

				heappush(minHeap,headCurrList)

		dummy = ListNode()

		currResultList = dummy

		while len(minHeap) > 0:

			currResultList.next = heappop(minHeap)

			currResultList = currResultList.next

			if currResultList.next:

				heappush(minHeap,currResultList.next)

		return dummy.next
			
			