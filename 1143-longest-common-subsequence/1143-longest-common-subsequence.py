class Solution:

	def longestCommonSubsequence(self,firstStr,secondStr):

		def helper(firstIndex,secondIndex,cache):

			if firstIndex < 0 or secondIndex < 0:

				return 0

			if (firstIndex,secondIndex) in cache:

				return cache[(firstIndex,secondIndex)]

			match = 1 + helper(firstIndex-1,secondIndex-1,cache) if firstStr[firstIndex] == secondStr[secondIndex] else 0
			notMatch = max(helper(firstIndex-1,secondIndex,cache),helper(firstIndex,secondIndex-1,cache))

			cache[(firstIndex,secondIndex)] = max(match,notMatch)
			return cache[(firstIndex,secondIndex)]

		return helper(len(firstStr)-1,len(secondStr)-1,{})