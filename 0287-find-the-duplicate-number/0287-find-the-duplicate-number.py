class Solution:

	def findDuplicate(self, nums):

		slowPointer = fastPointer = nums[0]

		while True:

			slowPointer = nums[slowPointer]
			fastPointer = nums[nums[fastPointer]]

			if slowPointer == fastPointer:
				break

		currPointer = nums[0]

		while currPointer != slowPointer:
			slowPointer = nums[slowPointer]
			currPointer = nums[currPointer]

		return currPointer
			