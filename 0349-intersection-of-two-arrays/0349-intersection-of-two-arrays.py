class Solution:

	def intersection(self, nums1, nums2):

		if len(nums2) < len(nums1):

			return self.intersection(nums2, nums1)

		numSet = set()

		for num in nums1:

			numSet.add(num)

		result = []

		for num in nums2:

			if num in numSet:

				result.append(num)
				numSet.remove(num)

		return result