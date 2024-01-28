class Solution:

	def isMatch(self,firstStr,secondStr):

		return self.helper(firstStr,secondStr,len(firstStr),len(secondStr),{})

	def helper(self,firstStr,secondStr,firstIndex,secondIndex,cache):

		if firstIndex == 0 and secondIndex == 0:

			return True

		if secondIndex == 0:

			return False

		if firstIndex == 0:

			for currIndex in range(1,secondIndex+1):

				if secondStr[currIndex-1] != '*':

					return False

			return True

		if (firstIndex,secondIndex) in cache:

			return cache[(firstIndex,secondIndex)]

		if firstStr[firstIndex-1] == secondStr[secondIndex-1] or secondStr[secondIndex-1] == '?':

			cache[(firstIndex,secondIndex)] = self.helper(firstStr,secondStr,firstIndex-1,secondIndex-1,cache)
			return cache[(firstIndex,secondIndex)]

		if secondStr[secondIndex-1] == '*':

			cache[(firstIndex,secondIndex)] = self.helper(firstStr,secondStr,firstIndex,secondIndex-1,cache) or self.helper(firstStr,secondStr,firstIndex-1,secondIndex,cache)
			return cache[(firstIndex,secondIndex)]

		cache[(firstIndex,secondIndex)] = False
		return cache[(firstIndex,secondIndex)]

			