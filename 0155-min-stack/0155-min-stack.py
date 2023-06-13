class MinStack:

	def __init__(self):

		self.stack = []

	def push(self, element):

		currMin = min(element, element if not self.stack else self.stack[-1][1])
		self.stack.append((element,currMin))
		

	def pop(self):

		return self.stack.pop()[0]

	def top(self):

		return self.stack[-1][0]

	def getMin(self):

		return self.stack[-1][1]
		