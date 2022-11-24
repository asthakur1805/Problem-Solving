class Solution:

	def sortedArrayToBST(self, nums):

		return self.helper(nums, 0, len(nums)-1)

	def helper(self, nums, leftPointer, rightPointer):

		if leftPointer > rightPointer:

			return

		midPointer = leftPointer + (rightPointer - leftPointer) // 2

		root = TreeNode(nums[midPointer])

		root.left = self.helper(nums, leftPointer, midPointer-1)

		root.right = self.helper(nums, midPointer+1, rightPointer)

		return root