class Solution:

	def wordBreak(self,inputStr,wordDict):

		wordSet = set(wordDict)

		return self.helper(inputStr,0,wordSet,{})

	def helper(self,inputStr,start,wordSet,cache):

		if start == len(inputStr):

			return True

		if start in cache:

			return cache[start]

		for end in range(start,len(inputStr)):

			if inputStr[start:end+1] in wordSet and self.helper(inputStr,end+1,wordSet,cache):

				cache[start] = True
				return cache[start]

		cache[start] = False
		return cache[start]