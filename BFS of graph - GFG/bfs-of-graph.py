from collections import deque

class Solution:

	def bfsOfGraph(self, numberNodes, graph):

		queue = deque([0])

		visited = set({0})

		result = []

		while queue:

			for _ in range(len(queue)):

				currNode = queue.popleft()

				result.append(currNode)

				for neighborNode in graph[currNode]:

					if neighborNode not in visited:

						queue.append(neighborNode)
						visited.add(neighborNode)

		return result
				


#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends