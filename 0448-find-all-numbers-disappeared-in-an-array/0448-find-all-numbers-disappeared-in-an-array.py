class Solution:

	def findDisappearedNumbers(self,nums):

		numSet = set()

		for num in nums:

			numSet.add(num)

		result = []

		for num in range(1,len(nums)+1):

			if num not in numSet:

				result.append(num)

		return result

		

		