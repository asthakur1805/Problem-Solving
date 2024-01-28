class Solution:

	def isMatch(self,firstStr,secondStr):

		prev = [False]*(len(secondStr)+1)
		prev[0] = True

		for secondIndex in range(1,len(secondStr)+1):

			for currIndex in range(1,secondIndex+1):

				if secondStr[currIndex-1] != '*':

					prev[secondIndex] = False
					break

			else:

				prev[secondIndex] = True

		for firstIndex in range(1,len(firstStr)+1):

			dp = [False]*(len(secondStr)+1)

			for secondIndex in range(1,len(secondStr)+1):

				if firstStr[firstIndex-1] == secondStr[secondIndex-1] or secondStr[secondIndex-1] == '?':

					dp[secondIndex] = prev[secondIndex-1]

				elif secondStr[secondIndex-1] == '*':

					dp[secondIndex] = dp[secondIndex-1] or prev[secondIndex]
					
				else:

					dp[secondIndex] = False

			prev = dp

		return prev[len(secondStr)]
				
