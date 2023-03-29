class Solution:

	def intersection(self, nums1, nums2):

		nums1.sort()
		nums2.sort()

		firstIndex, secondIndex = 0, 0

		result = []

		while firstIndex < len(nums1) and secondIndex < len(nums2):

			if nums1[firstIndex] < nums2[secondIndex]:

				firstIndex += 1

			elif nums2[secondIndex] < nums1[firstIndex]:

				secondIndex += 1

			else:

				if not result or result[-1] != nums1[firstIndex]:

					result.append(nums1[firstIndex])

				firstIndex += 1

				secondIndex += 1

		return result