from collections import defaultdict

class Solution:

	def verticalTraversal(self,root):

		if not root:

			return

		# (node,vertical,level)

		queue = deque([(root,0,0)])

		# vertical : [(level, nodeVal)]

		verticalNodes = defaultdict(list)

		minVertical, maxVertical = 0, 0

		while queue:

			for _ in range(len(queue)):

				node, vertical, level = queue.popleft()

				minVertical, maxVertical = min(minVertical,vertical), max(maxVertical,vertical)

				verticalNodes[vertical].append((level,node.val))

				if node.left:

					queue.append((node.left,vertical-1,level+1))

				if node.right:

					queue.append((node.right,vertical+1,level+1))

		result = []

		for vertical in range(minVertical,maxVertical+1):

			verticalResult = []

			for verticalNode in sorted(verticalNodes[vertical]):

				verticalResult.append(verticalNode[1])

			result.append(verticalResult)

		return result
			
			