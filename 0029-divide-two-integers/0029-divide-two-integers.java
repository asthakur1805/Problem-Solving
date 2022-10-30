class Solution
{
	public int divide(int dividend, int divisor) 
	{
		
        if (dividend == Integer.MIN_VALUE && divisor == -1)
            return Integer.MAX_VALUE;
        
        int sign = (dividend > 0)==(divisor > 0)? 1: -1;

		dividend = Math.abs(dividend);
		divisor = Math.abs(divisor);
        int quotient = 0;

		while (dividend - divisor >= 0)
		{
			short power = 0;
			while (dividend - (divisor << 1 << power) >= 0) 
			{
				power += 1;
			}
			
            quotient += (1 << power);
            dividend -= (divisor << power);
            
            
		}

        return sign * quotient;

	}
}