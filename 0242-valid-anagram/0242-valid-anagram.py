class Solution:

	def isAnagram(self, firstStr, secondStr):

		from collections import Counter

		return Counter(firstStr) == Counter(secondStr)
