class Solution:

	def shortestCommonSupersequence(self,firstStr,secondStr):

		dp = [[0]*(len(secondStr)+1) for _ in range(len(firstStr)+1)]

		for firstIndex in range(1,len(firstStr)+1):

			for secondIndex in range(1,len(secondStr)+1):

				if firstStr[firstIndex-1] == secondStr[secondIndex-1]:

					dp[firstIndex][secondIndex] = 1 + dp[firstIndex-1][secondIndex-1]

				else:
						
					dp[firstIndex][secondIndex] = max(dp[firstIndex-1][secondIndex],dp[firstIndex][secondIndex-1])
			
		firstIndex, secondIndex = len(firstStr), len(secondStr)

		lcsLength = dp[firstIndex][secondIndex]

		scsLength = len(firstStr)+len(secondStr)-lcsLength

		updateIndex = scsLength-1

		result = [None] * scsLength 

		while firstIndex > 0 and secondIndex > 0:

			if firstStr[firstIndex-1] == secondStr[secondIndex-1]:

				result[updateIndex] = firstStr[firstIndex-1]
				firstIndex -= 1
				secondIndex -= 1

			elif dp[firstIndex-1][secondIndex] > dp[firstIndex][secondIndex-1]:

				result[updateIndex] = firstStr[firstIndex-1]
				firstIndex -= 1

			else:

				result[updateIndex] = secondStr[secondIndex-1]
				secondIndex -= 1

			updateIndex -= 1

		while firstIndex > 0:

			result[updateIndex] = firstStr[firstIndex-1]
			firstIndex -= 1
			updateIndex -= 1

		while secondIndex > 0:

			result[updateIndex] = secondStr[secondIndex-1]
			secondIndex -= 1
			updateIndex -= 1

		return ''.join(result)