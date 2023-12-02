class Solution:

	def findMedianSortedArrays(self,firstArr,secondArr):

		total = len(firstArr)+len(secondArr)
		half = total // 2

		if len(firstArr) > len(secondArr):

			firstArr, secondArr = secondArr, firstArr

		left, right = 0, len(firstArr)-1

		while True:

			firstPartition = left + (right-left) // 2

			secondPartition = half - (firstPartition+1) - 1

			firstArrLeft = firstArr[firstPartition] if firstPartition >= 0 else float('-inf')
			firstArrRight = firstArr[firstPartition+1] if (firstPartition+1) < len(firstArr) else float('inf')
			secondArrLeft = secondArr[secondPartition] if secondPartition >= 0 else float('-inf')
			secondArrRight = secondArr[secondPartition+1] if (secondPartition+1) < len(secondArr) else float('inf')

			if firstArrLeft <= secondArrRight and secondArrLeft <= firstArrRight:

				if total % 2:

					return min(firstArrRight,secondArrRight)

				return (max(firstArrLeft,secondArrLeft)+min(firstArrRight,secondArrRight)) / 2

			elif firstArrLeft > secondArrRight:

				right = firstPartition - 1

			else:

				left = firstPartition + 1
	