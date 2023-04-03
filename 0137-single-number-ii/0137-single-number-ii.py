class Solution:

	def singleNumber(self, nums):

		result = 0

		for bitPosition in range(32):

			setBitCount, mask = 0, (1 << bitPosition)

			for num in nums:

				if num & mask:

					setBitCount += 1

			if setBitCount % 3:

				if result + mask >= (1 << 31):

					result += mask - (1 << 32)

				else:

					result += mask

		return result
	