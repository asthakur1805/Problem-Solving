from collections import deque

class Solution:

	def maxLevelSum(self,root):

		queue = deque([root])

		result, maxSum, currLevel = 0, float(-inf), 1

		while queue:

			currSum = 0

			for _ in range(len(queue)):

				node = queue.popleft()

				currSum += node.val

				if node.left:

					queue.append(node.left)

				if node.right:

					queue.append(node.right)

			if currSum > maxSum:

				maxSum, result = currSum, currLevel

			currLevel += 1

		return result

		