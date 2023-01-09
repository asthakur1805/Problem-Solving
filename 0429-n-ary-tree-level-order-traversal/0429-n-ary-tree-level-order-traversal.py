class Solution:

	def levelOrder(self, root):

		if not root:

			return

		result = []

		queue = collections.deque([root])

		while queue:

			level = []

			for _ in range(len(queue)):

				node = queue.popleft()

				level.append(node.val)

				for childNode in node.children:

					queue.append(childNode)

			result.append(level)

		return result