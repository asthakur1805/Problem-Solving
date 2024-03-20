class Solution:

	def numRescueBoats(self,people,limit):

		people.sort()

		left, right = 0, len(people)-1

		boats = 0

		while left <= right:

			remaining = limit - people[right]

			boats += 1
			right -= 1

			if people[left] <= remaining:

				left += 1

		return boats