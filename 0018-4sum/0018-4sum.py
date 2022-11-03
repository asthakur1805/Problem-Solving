class Solution:

	def fourSum(self, nums, target):

		nums.sort()

		result, builder = [], []

		self.helper(nums, target, 4, 0, builder, result)

		return result

	def helper(self, nums, target, K, index, builder, result):

		if K != 2:

			for currIndex in range(index, len(nums)-K+1):

				if currIndex > index and nums[currIndex] == nums[currIndex-1]:

					continue

				builder.append(nums[currIndex])

				self.helper(nums, target - nums[currIndex], K-1, currIndex+1, builder, result)

				builder.pop()

			return

		leftPointer, rightPointer = index, len(nums)-1

		while leftPointer < rightPointer:

			addition = nums[leftPointer] + nums[rightPointer]

			if addition < target:

				leftPointer += 1

			elif addition > target:

				rightPointer -= 1

			else:

				builder.append(nums[leftPointer])
				builder.append(nums[rightPointer])

				result.append(builder.copy())

				for _ in range(2):
					builder.pop()

				leftPointer += 1

				while leftPointer < rightPointer and nums[leftPointer]==nums[leftPointer-1]:

					leftPointer += 1

		return

				

			