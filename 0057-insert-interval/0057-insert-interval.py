class Solution:

	def insert(self, intervals, newInterval):

		result = []

		for index, currInterval in enumerate(intervals):

			currStart, currEnd, newStart, newEnd = currInterval[0], currInterval[1], newInterval[0], newInterval[1]

			if newEnd < currStart:

				result.append(newInterval)

				return result + intervals[index:]

			elif newStart > currEnd:

				result.append(currInterval)

			else:

				newInterval[0], newInterval[1] = min(currStart, newStart), max(currEnd, newEnd)

		result.append(newInterval)

		return result