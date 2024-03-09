class Solution:

	def isMatch(self,inputStr,pattern):

		dp = [[False]*(len(pattern)+1) for _ in range(len(inputStr)+1)]

		for strIndex in range(len(inputStr),-1,-1):

			for patIndex in range(len(pattern),-1,-1):

				if strIndex == len(inputStr) and patIndex == len(pattern):

					dp[strIndex][patIndex] = True 

				elif patIndex < len(pattern):

					match = strIndex < len(inputStr) and (inputStr[strIndex] == pattern[patIndex] or pattern[patIndex] == '.')

					if patIndex+1<len(pattern) and pattern[patIndex+1] == '*':

						dp[strIndex][patIndex] = dp[strIndex][patIndex+2] or match and dp[strIndex+1][patIndex]

					elif match:

						dp[strIndex][patIndex] = dp[strIndex+1][patIndex+1]

		return dp[0][0]