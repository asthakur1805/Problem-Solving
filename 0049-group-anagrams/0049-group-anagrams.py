class Solution:

	def groupAnagrams(self, inputStrs):

		from collections import defaultdict

		groups = defaultdict(list)

		for inputStr in inputStrs:

			counts = {}

			for char in inputStr:

				counts[char] = counts.get(char, 0) + 1

			groups[frozenset(counts.items())].append(inputStr)

		return groups.values()