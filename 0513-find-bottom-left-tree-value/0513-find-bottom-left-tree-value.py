from collections import deque

class Solution:

	def findBottomLeftValue(self,root):

		if not root:

			return

		queue = deque([root])

		while queue:

			resultNode = queue[0]

			for _ in range(len(queue)):

				node = queue.popleft()

				if node.left:

					queue.append(node.left)

				if node.right:

					queue.append(node.right)

		return resultNode.val