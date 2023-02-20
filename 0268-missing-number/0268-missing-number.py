class Solution:

	def missingNumber(self, inputNums):

		visitedNums = set()

		for num in inputNums:

			visitedNums.add(num)

		for number in range(len(inputNums)+1):

			if number not in visitedNums:

				return number