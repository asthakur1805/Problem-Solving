class Solution:

	def sortedArrayToBST(self, nums):

		leftPointer, rightPointer = 0, len(nums)-1

		return self.helper(nums, leftPointer, rightPointer)
	
	def helper(self, nums, leftPointer, rightPointer):

		if leftPointer > rightPointer:

			return

		midPointer = leftPointer + (rightPointer - leftPointer) // 2

		root = TreeNode(nums[midPointer])

		root.left, root.right = self.helper(nums, leftPointer, midPointer-1), self.helper(nums, midPointer+1, rightPointer)

		return root