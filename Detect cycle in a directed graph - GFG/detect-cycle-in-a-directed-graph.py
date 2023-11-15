from collections import deque

class Solution:

	def isCyclic(self,numberNodes,adjList):

		numberNodes = len(adjList)

		indegree, queue, topoResult = {node:0 for node in range(numberNodes)}, deque([]), []

		for currNode in range(numberNodes):

			for neighborNode in adjList[currNode]:

				indegree[neighborNode] += 1

		for node, degree in indegree.items():

			if degree == 0:

				queue.append(node)

		while queue:

			currNode = queue.popleft()

			topoResult.append(currNode)

			for neighborNode in adjList[currNode]:

				indegree[neighborNode] -= 1

				if indegree[neighborNode] == 0:

					queue.append(neighborNode)

		return len(topoResult) != numberNodes



				

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