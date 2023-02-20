class Solution:

	def missingNumber(self, inputNums):

		result = 0

		for index in range(len(inputNums)):

			result += index - inputNums[index]

		return result + len(inputNums)