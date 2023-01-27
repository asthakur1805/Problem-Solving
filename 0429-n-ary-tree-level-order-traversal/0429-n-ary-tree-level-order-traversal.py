class Solution:

	def levelOrder(self, root):

		if not root:

			return

		queue = collections.deque([root])

		result = []

		while queue:

			level = []

			for _ in range(len(queue)):

				node = queue.popleft()

				level.append(node.val)

				for childNode in node.children:

					queue.append(childNode)

			result.append(level)

		return result

			