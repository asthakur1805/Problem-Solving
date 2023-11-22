class Solution:

	def firstBadVersion(self,numberVersions):

		left, right = 1, numberVersions

		while left <= right:

			mid = left + (right - left) // 2

			if isBadVersion(mid):

				result = mid

				right = mid - 1

			else:

				left = mid + 1

		return result