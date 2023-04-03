class Solution:

	def strStr(self, haystack, needle):

		haystackLength, needleLength = len(haystack), len(needle)

		for haystackIndex in range(haystackLength-needleLength+1):

			for needleIndex in range(needleLength):

				if haystack[haystackIndex + needleIndex] != needle[needleIndex]:

					break

			else:

				return haystackIndex

		return -1