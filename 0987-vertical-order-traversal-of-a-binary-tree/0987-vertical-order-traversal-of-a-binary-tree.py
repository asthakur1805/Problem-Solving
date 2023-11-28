from collections import defaultdict

class Solution:

	def verticalTraversal(self,root):

		if not root:

			return

		stack, result = [(root,0,0)], []

		minVertical, maxVertical = float('inf'), float('-inf')

		verticalMap = defaultdict(list)

		while stack:

			node,vertical,level = stack.pop()

			minVertical, maxVertical = min(minVertical,vertical), max(maxVertical,vertical)

			verticalMap[vertical].append((level,node.val))

			if node.right:

				stack.append((node.right,vertical+1,level+1))

			if node.left:

				stack.append((node.left,vertical-1,level+1))

		for vertical in range(minVertical,maxVertical+1):

			verticalResult = []

			for _ , verticalNode in sorted(verticalMap[vertical]):

				verticalResult.append(verticalNode)

			result.append(verticalResult)

		return result