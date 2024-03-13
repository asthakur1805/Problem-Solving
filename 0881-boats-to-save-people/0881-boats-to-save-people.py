class Solution:

	def numRescueBoats(self,people,limit):

		people.sort()

		left, right = 0, len(people)-1

		result = 0

		while left <= right:

			remaining = limit-people[right]
			result += 1
			right -= 1

			if people[left] <= remaining:

				left += 1

		return result
			