from heapq import heapify, heappush, heappop

class Solution:

	def reorganizeString(self,inputStr):

		counts = {}

		for currChar in inputStr:

			counts[currChar] = counts.get(currChar,0) + 1

		maxHeap = [(-count,currChar) for currChar, count in counts.items()]

		heapify(maxHeap)

		prev, result = '', [] 

		while maxHeap:

			count, currChar = heappop(maxHeap)
			result.append(currChar)
			count += 1

			if prev:

				heappush(maxHeap,prev)
				prev = ''

			if count:

				prev = (count,currChar)

		return ''.join(result) if not prev else ''
		
				
				