'''
File: number-of-1-bits.py
##################################
           Question               
##################################
  Problem statement
  Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

  Example 1:

  Input: n = 11

  Output: 3

  Explanation:

  The input binary string 1011 has a total of three set bits.

  Example 2:

  Input: n = 128

  Output: 1

  Explanation:

  The input binary string 10000000 has a total of one set bit.

  Example 3:

  Input: n = 2147483645

  Output: 30

  Explanation:

  The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

  

  Constraints:

  1 <= n <= 2^(31 - 1)
  

  Follow up: If this function is called many times, how would you optimize it?
##################################
           Learnings               
##################################
  Key insight
  Right Shift >> divids the number by 2 and also remove one bit from the number
'''
class Solution(object):
  def hammingWeight(self, n):
    """
    :type n: int
    :rtype: int
    """
    count = 0
    mask = 0xFFFFFFFE
    while (True):
      if n | mask == 0xFFFFFFFF:
        count += 1
      n >>= 1
      if n == 0:
        break   
    return count     
        

if __name__ == '__main__':
  object = Solution()
  print(Solution().hammingWeight(128))
   