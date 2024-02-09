class Solution:

	def numSquares(self,inputNumber):

		dp = [inputNumber] * (inputNumber+1)

		dp[0] = 0

		for index in range(1,len(dp)):

			currNumber = 1 

			while currNumber * currNumber <= inputNumber:

				dp[index] = min(dp[index],1+dp[index-currNumber*currNumber])

				currNumber += 1

		return dp[inputNumber]