class Solution:

	def merge(self, intervals):

		if not intervals:

			return

		intervals.sort(key=lambda interval:interval[0])

		result = [intervals[0]]

		for currStart, currEnd in intervals[1:]:

			lastEnd = result[-1][1]

			if currStart <= lastEnd:

				result[-1][1] = max(currEnd, lastEnd)

			else:

				result.append([currStart, currEnd])

		return result

		

			

		