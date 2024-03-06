class Solution:

	def compareLengths(self,firstWord,secondWord):

		return -1 if len(firstWord) <= len(secondWord) else 1

	def longestStrChain(self,words):

		words.sort(key=cmp_to_key(self.compareLengths))

		dp = [1]*len(words)

		resultLength = 1

		for currIndex in range(1,len(words)):

			for prevIndex in range(currIndex):

				if self.doesFormChain(words[prevIndex],words[currIndex]) and dp[prevIndex]+1 > dp[currIndex]:

					dp[currIndex] = dp[prevIndex] + 1

			resultLength = max(resultLength,dp[currIndex])

		return resultLength

	def doesFormChain(self,prevWord,currWord):

		if len(prevWord)+1 != len(currWord):

			return False

		prevIndex, currIndex = 0, 0

		while currIndex < len(currWord):

			if prevIndex < len(prevWord) and prevWord[prevIndex] == currWord[currIndex]:

				prevIndex += 1

			currIndex += 1

		return prevIndex == len(prevWord) and currIndex == len(currWord)