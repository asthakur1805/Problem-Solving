class Solution:

	def wordBreak(self,inputStr,wordDict):

		wordSet = set(wordDict)

		dp = [False] * (len(inputStr)+1)

		dp[len(inputStr)] = True

		for start in range(len(inputStr)-1,-1,-1):

			for end in range(start,len(inputStr)):

				if inputStr[start:end+1] in wordSet and dp[end+1]:

					dp[start] = True
					break

		return dp[0]