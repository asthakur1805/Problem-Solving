class MinStack:

	def __init__(self):

		self.stack = []

	def push(self, element):

		currMin = element if not self.stack else min(element, self.stack[-1][1])
  
		self.stack.append((element, currMin))

	def pop(self):

		return self.stack.pop()[0] if self.stack else None

	def top(self):

		return self.stack[-1][0] if self.stack else None

	def getMin(self):

		return self.stack[-1][1] if self.stack else None