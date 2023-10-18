from collections import deque

class Solution:

	def bfsOfGraph(self,numberNodes,adjList):

		queue, visited, result = deque([0]), set({0}), []

		while queue:

			currNode = queue.popleft()

			result.append(currNode)

			for neighborNode in adjList[currNode]:

				if neighborNode not in visited:

					visited.add(neighborNode)
					queue.append(neighborNode)

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