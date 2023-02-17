class Solution:

	def isAnagram(self, firstStr, secondStr):

		return Counter(firstStr) == Counter(secondStr)
			