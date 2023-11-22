class BSTIterator:

	def __init__(self,root):

		self.stack = []

		curr = root

		self.helper(curr)

	def next(self):

		curr = self.stack.pop()

		result = curr.val

		curr = curr.right

		self.helper(curr)

		return result


	def hasNext(self):

		return len(self.stack) > 0

	def helper(self,curr):

		while curr:

			self.stack.append(curr)

			curr = curr.left