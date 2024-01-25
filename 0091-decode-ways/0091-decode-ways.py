class Solution:

	def numDecodings(self,inputStr):

		dp = [0]*(len(inputStr)+1)

		dp[len(inputStr)] = 1

		for start in range(len(inputStr)-1,-1,-1):

			if inputStr[start] == '0':

				dp[start] = 0

			else:

				singlePartition = dp[start+1]

				doublePartition = dp[start+2] if start+1<len(inputStr) and (inputStr[start] == '1' or inputStr[start] == '2' and '0' <= inputStr[start+1] <= '6') else 0

				dp[start] = singlePartition+doublePartition

		return dp[0]



		
		