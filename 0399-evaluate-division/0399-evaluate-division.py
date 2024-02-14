from collections import deque

class Solution:

	def calcEquation(self,equations,values,queries):

		adjList = {}

		for index in range(len(equations)):

			[numerator, denominator] = equations[index]
			currValue = values[index]

			if numerator not in adjList:

				adjList[numerator] = []

			if denominator not in adjList:

				adjList[denominator] = []

			adjList[numerator].append((denominator,currValue))
			adjList[denominator].append((numerator,1/currValue))

		result = []

		for [numerator,denominator] in queries:

			result.append(self.bfs(adjList,numerator,denominator))

		return result

	def bfs(self,adjList,numerator,denominator):

		if numerator not in adjList or denominator not in adjList:

			return -1

		queue = deque([(numerator,1)])
		visited = set({numerator})

		while queue:

			currChar, currProduct = queue.popleft()

			if currChar == denominator:

				return currProduct

			for neighborChar, neighborValue in adjList[currChar]:

				if neighborChar not in visited:

					queue.append((neighborChar,currProduct*neighborValue))
					visited.add(neighborChar)

		return -1

		

		