from collections import deque

class Solution:

	def isCyclic(self,numberNodes, graph):

		indegree = {num:0 for num in range(len(graph))}

		for parentNode in range(len(graph)):

			for neighborNode in graph[parentNode]:

				indegree[neighborNode] += 1

		result, queue = [], deque([])

		for node, degree in indegree.items():

			if degree == 0:

				queue.append(node)

		while queue:

			currNode = queue.popleft()

			result.append(currNode)

			for neighborNode in graph[currNode]:

				indegree[neighborNode] -= 1

				if indegree[neighborNode] == 0:

					queue.append(neighborNode)

		return len(result) < len(graph)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends