class Solution:

	def maxArea(self, heights):

		leftPointer, rightPointer = 0, len(heights)-1

		resultArea = 0

		while leftPointer < rightPointer:

			currentArea = (rightPointer - leftPointer) * min(heights[leftPointer], heights[rightPointer])

			resultArea = max(currentArea, resultArea)

			if heights[leftPointer] < heights[rightPointer]:

				leftPointer += 1

			else:

				rightPointer -= 1

		return resultArea