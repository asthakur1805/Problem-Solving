class Solution:

	def insert(self, intervals, newInterval):
	
		result = []

		for index, interval in enumerate(intervals):

			if newInterval[1] < interval[0]:

				result.append(newInterval)

				return result + intervals[index:]

			elif interval[1] < newInterval[0]:

				result.append(interval)

			else:

				newInterval[0],newInterval[1] = min(interval[0],newInterval[0]), max(interval[1], newInterval[1])

		result.append(newInterval)

		return result