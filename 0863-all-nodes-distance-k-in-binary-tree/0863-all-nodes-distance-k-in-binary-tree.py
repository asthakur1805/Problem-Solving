from collections import deque

class Solution:

	def distanceK(self,root,target,distance):

		if not root:

			return

		queue = deque([root])
		parentMap = {}

		while queue:

			currNode = queue.popleft()
	
			if currNode.val == target.val:
				
				break

			if currNode.left:

				parentMap[currNode.left] = currNode
				queue.append(currNode.left)
				

			if currNode.right:

				parentMap[currNode.right] = currNode
				queue.append(currNode.right)

		queue = deque([currNode])
		visited = set({currNode})

		while queue and distance > 0:

			for _ in range(len(queue)):

				currNode = queue.popleft()

				if parentMap.get(currNode,None) and parentMap[currNode] not in visited:

					queue.append(parentMap[currNode])
					visited.add(parentMap[currNode])

				if currNode.left and currNode.left not in visited:

					queue.append(currNode.left)
					visited.add(currNode.left)
	
				if currNode.right and currNode.right not in visited:

					queue.append(currNode.right)
					visited.add(currNode.right)

			distance -= 1

		return [currNode.val for currNode in queue]

			
		