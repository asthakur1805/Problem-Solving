class Solution:

	def maxProduct(self,nums):

		currMax, currMin, result = 1, 1, float('-inf')

		for num in nums:

			product = currMax*num 
	
			currMax = max(product,currMin*num,num)
			currMin = min(product,currMin*num,num)

			result = max(result,currMax)

			if num == 0:

				currMax, currMin = 1, 1

		return result

		