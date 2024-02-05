from collections import deque

class Solution:

	def widthOfBinaryTree(self,root):

		queue = deque([(root,0)])

		result = float('-inf')

		while queue:

			minIndex, maxIndex = queue[0][1], queue[-1][1]

			result = max(result,maxIndex-minIndex+1)

			for _ in range(len(queue)):

				node, currIndex = queue.popleft()

				if node.left:

					queue.append((node.left,2*(currIndex-minIndex)+1))

				if node.right:

					queue.append((node.right,2*(currIndex-minIndex)+2))

		return result