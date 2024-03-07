class Solution:

	def longestStrChain(self,words):

		mapping = {word:index for index,word in enumerate(words)}

		cache = {}

		for wordIndex in range(len(words)):

			self.dfs(words,wordIndex,mapping,cache)

		return max(cache.values())

		

	def dfs(self,words,wordIndex,mapping,cache):

		if wordIndex in cache:

			return cache[wordIndex]

		result = 1

		currWord = words[wordIndex]

		for charIndex in range(len(currWord)):

			prevWord = currWord[:charIndex]+currWord[charIndex+1:]

			if prevWord in mapping:

				result = max(result,1 + self.dfs(words,mapping[prevWord],mapping,cache))

		cache[wordIndex] = result
		return result

	