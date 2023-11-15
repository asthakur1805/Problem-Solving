class Solution:

	def eventualSafeNodes(self,adjList):

		numberNodes = len(adjList)

		visited, result = [0]*numberNodes, []

		for startNode in range(numberNodes):

			if visited[startNode] == 0:

				self.dfs(adjList,startNode,visited)

		for currNode in range(numberNodes):

			if visited[currNode] == 1:

				result.append(currNode)

		return result

	def dfs(self,adjList,currNode,visited):

		visited[currNode] = 2

		for neighborNode in adjList[currNode]:

			if (visited[neighborNode] == 0 and self.dfs(adjList,neighborNode,visited)) or visited[neighborNode] == 2:

				return

		visited[currNode] = 1

	