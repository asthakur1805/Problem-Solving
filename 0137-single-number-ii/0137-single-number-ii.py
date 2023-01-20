class Solution:

	def singleNumber(self, nums):

		result = 0

		for bitPosition in range(32):

			mask = (1 << bitPosition)

			count = 0

			for num in nums:

				if num & mask:

					count += 1

			if count % 3:

				if result + mask < (2 ** 31):

					result += mask

				else:

					result += mask - (2 ** 32)

		return result