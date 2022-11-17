class Solution:

	def merge(self, intervals):

		intervals.sort(key=lambda interval: interval[0])

		result = [intervals[0]]

		for intervalIndex in range(1, len(intervals)):

			currStart, currEnd = intervals[intervalIndex]

			lastEnd = result[-1][1]

			if lastEnd >= currStart:

				result[-1][1] = max(lastEnd, currEnd)

			else:

				result.append([currStart, currEnd])


		return result