from collections import deque

class Solution:

	def largestValues(self,root):

		if not root:

			return 

		queue, result = deque([root]), []

		while queue:

			levelMax = float('-inf')

			for _ in range(len(queue)):

				node = queue.popleft()

				levelMax = max(levelMax,node.val)

				if node.left:

					queue.append(node.left)

				if node.right:

					queue.append(node.right)

			result.append(levelMax)

		return result