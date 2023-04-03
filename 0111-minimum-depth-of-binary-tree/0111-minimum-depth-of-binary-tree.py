class Solution:

	def minDepth(self, root):

		if not root:

			return 0

		queue = collections.deque([(root, 1)])

		while queue:

			for _ in range(len(queue)):

				node, depth = queue.popleft()

				if not node.left and not node.right:

					return depth

				if node.left:

					queue.append((node.left, depth+1))

				if node.right:

					queue.append((node.right, depth+1))

