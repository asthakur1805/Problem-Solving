class Solution:

	def groupAnagrams(self, inputStrs):

		from collections import defaultdict

		anagrams = defaultdict(list)

		for currStr in inputStrs:

			counts = [0] * 26

			for char in currStr:

				counts[ord(char)-ord('a')] += 1

			anagrams[tuple(counts)].append(currStr)

		return anagrams.values()