#User function Template for python3

class Solution:

	def dfsOfGraph(self, v, adjList):

		result = []

		visited = set()

		self.helper(0, result, visited, adjList)

		return result

	def helper(self, node, result, visited, adjList):

		result.append(node)

		visited.add(node)

		for neighbor in adjList[node]:

			if neighbor not in visited:

				self.helper(neighbor, result, visited, adjList)


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends