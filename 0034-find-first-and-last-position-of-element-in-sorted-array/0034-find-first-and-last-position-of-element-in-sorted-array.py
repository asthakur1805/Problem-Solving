class Solution:

	def searchRange(self, nums, target):

		firstIndex, lastIndex = -1, -1

		left, right = 0, len(nums)-1

		while left <= right:

			mid = left + (right - left) // 2

			if nums[mid] == target:

				firstIndex = mid

				right = mid - 1

			elif nums[mid] < target:

				left = mid + 1

			else:

				right = mid - 1

		if firstIndex == -1:

			return [firstIndex, lastIndex]

		left, right = 0, len(nums)-1

		while left <= right:

			mid = left + (right - left) // 2

			if nums[mid] == target:

				lastIndex = mid

				left = mid + 1

			elif nums[mid] < target:

				left = mid + 1

			else:

				right = mid - 1

		return [firstIndex, lastIndex]