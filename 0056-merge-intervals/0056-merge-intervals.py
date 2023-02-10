class Solution:

	def merge(self, intervals):

		if not intervals:

			return

		intervals.sort(key=lambda interval:interval[0])

		result = [intervals[0]]

		for index in range(1, len(intervals)):

			interval = intervals[index]

			currentStart, currentEnd = interval[0], interval[1]

			lastEnd = result[-1][1]

			if currentStart <= lastEnd:
				
				result[-1][1] = max(currentEnd, lastEnd)

			else:

				result.append(interval)

		return result