from random import randint

class Solution:

	def __init__(self,nums):

		self.runningSum = [nums[0]]

		for index in range(1,len(nums)):

			self.runningSum.append(nums[index]+self.runningSum[index-1])

	def pickIndex(self):

		choice = randint(1,self.runningSum[-1])

		left, right = 0, len(self.runningSum)-1

		while left <= right:

			mid = left + (right - left) // 2

			if self.runningSum[mid] == choice:

				return mid

			if self.runningSum[mid] < choice:

				left = mid + 1

			else:

				right = mid - 1

		return left



		