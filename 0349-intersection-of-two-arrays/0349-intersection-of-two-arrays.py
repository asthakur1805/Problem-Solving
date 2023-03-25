class Solution:

	def intersection(self, nums1, nums2):

		if len(nums2) < len(nums1):

			return self.intersection(nums2, nums1)

		numsSet = set()

		for num in nums1:

			numsSet.add(num)

		result = []

		for num in nums2:

			if num in numsSet:

				result.append(num)

				numsSet.remove(num)

		return result