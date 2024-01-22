class Solution:

	def longestCommonSubsequence(self,firstStr,secondStr):

		return self.helper(firstStr,secondStr,len(firstStr),len(secondStr),{})

	def helper(self,firstStr,secondStr,firstIndex,secondIndex,cache):

		if firstIndex == 0 or secondIndex == 0:

			return 0

		if (firstIndex,secondIndex) in cache:

			return cache[(firstIndex,secondIndex)]

		if firstStr[firstIndex-1] == secondStr[secondIndex-1]:

			cache[(firstIndex,secondIndex)] = 1 + self.helper(firstStr,secondStr,firstIndex-1,secondIndex-1,cache)
			return cache[(firstIndex,secondIndex)]

		cache[(firstIndex,secondIndex)] = max(self.helper(firstStr,secondStr,firstIndex-1,secondIndex,cache),self.helper(firstStr,secondStr,firstIndex,secondIndex-1,cache))
		return cache[(firstIndex,secondIndex)]


		
		
