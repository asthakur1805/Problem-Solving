class Solution:

	def groupAnagrams(self, inputStrs):

		from collections import defaultdict

		groups = defaultdict(list) 

		for inputStr in inputStrs:

			counts = [0] * 26

			for char in inputStr:

				counts[ord(char)-ord('a')] += 1

			groups[tuple(counts)].append(inputStr)

		return groups.values()