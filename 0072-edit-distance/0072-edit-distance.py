class Solution:

	def minDistance(self,firstStr,secondStr):

		prev = [0]*(len(secondStr)+1)

		for secondIndex in range(len(secondStr)+1):

			prev[secondIndex] = secondIndex

		for firstIndex in range(1,len(firstStr)+1):

			dp = [0]*(len(secondStr)+1)
			dp[0] = firstIndex

			for secondIndex in range(1,len(secondStr)+1):

				if firstStr[firstIndex-1] == secondStr[secondIndex-1]: 

					dp[secondIndex] = prev[secondIndex-1]

				else:

					insertion = dp[secondIndex-1]
					deletion = prev[secondIndex]
					replacement = prev[secondIndex-1]

					dp[secondIndex] = 1 + min(insertion,deletion,replacement)
			
			prev = dp

		return prev[len(secondStr)]