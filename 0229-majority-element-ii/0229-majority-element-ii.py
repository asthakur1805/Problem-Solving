class Solution:

	def majorityElement(self,nums):

		firstCandidate, firstCount, secondCandidate, secondCount = None, 0, None, 0

		for num in nums:

			if firstCandidate == num:

				firstCount += 1

			elif secondCandidate == num:

				secondCount += 1

			elif firstCount == 0:

				firstCandidate = num
				firstCount = 1

			elif secondCount == 0:

				secondCandidate = num
				secondCount = 1

			else:

				firstCount -= 1
				secondCount -= 1

		firstCount, secondCount = 0, 0

		for num in nums:

			if firstCandidate == num:

				firstCount += 1

			elif secondCandidate == num:

				secondCount += 1

		result = []

		if firstCount > len(nums)//3: 
			
			result.append(firstCandidate)

		
		if secondCount > len(nums)//3: 
			
			result.append(secondCandidate)

		return result
		

		
			