from collections import deque

class Solution:

	def maxLevelSum(self,root):

		queue = deque([root])

		resultSum, currLevel, resultLevel = -(1<<31), 0, 0

		while queue:

			currLevelSum = 0
			currLevel += 1

			for _ in range(len(queue)):

				node = queue.popleft()

				currLevelSum += node.val

				if node.left:

					queue.append(node.left)

				if node.right:

					queue.append(node.right)

			if currLevelSum > resultSum:

				resultSum, resultLevel = currLevelSum, currLevel
				

		return resultLevel
