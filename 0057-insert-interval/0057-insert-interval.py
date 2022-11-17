class Solution:

	def insert(self, intervals, newInterval):

		result = []

		for index in range(len(intervals)):

			if newInterval[1] < intervals[index][0]:

				result.append(newInterval)
				return result + intervals[index:]

			if newInterval[0] > intervals[index][1]:

				result.append(intervals[index])

			else:

				newInterval = [min(newInterval[0], intervals[index][0]), max(newInterval[1], intervals[index][1])]

		result.append(newInterval)

		return result