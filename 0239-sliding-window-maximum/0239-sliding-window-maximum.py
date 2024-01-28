from collections import deque

class Solution:

	def maxSlidingWindow(self,nums,windowSize):

		queue, result = deque([]), []
	
		for rearIndex, num in enumerate(nums):

			while queue and num > nums[queue[-1]]:

				queue.pop()

			queue.append(rearIndex)

			if rearIndex >= windowSize-1:

				frontIndex = queue[0]

				result.append(nums[frontIndex])
				
				if frontIndex == rearIndex-windowSize+1:

					queue.popleft()

		return result

		