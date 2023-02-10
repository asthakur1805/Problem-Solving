class Solution:

	def merge(self, intervals):

		if not intervals:

			return

		intervals.sort(key=lambda interval:interval[0])

		result = [intervals[0]]

		for index in range(1, len(intervals)):

			interval = intervals[index]

			currStart, currEnd = interval[0], interval[1]

			lastEnd = result[-1][1]

			if currStart <= lastEnd:

				result[-1][1] = max(currEnd, lastEnd)

			else:

				result.append(interval)

		return result