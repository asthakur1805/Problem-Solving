from collections import deque

class Solution:

	def bfsOfGraph(self, numberNodes, adjList):

		if not numberNodes:

			return 

		visited = set({0})
		queue = deque([0])

		result = []

		while queue:

			for _ in range(len(queue)):

				node = queue.popleft()

				result.append(node)

				for neighbor in adjList[node]:

					if neighbor not in visited:

						visited.add(neighbor)
						queue.append(neighbor)

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