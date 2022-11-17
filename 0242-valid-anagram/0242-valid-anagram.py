class Solution:

	def isAnagram(self, firstStr, secondStr):

		return sorted(firstStr) == sorted(secondStr)