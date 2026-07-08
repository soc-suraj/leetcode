
'''
File:  power-of-four.py
##################################
           Question               
##################################
  Problem statement

Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

Example 1:
Input: n = 16
Output: true

Example 2:
Input: n = 5
Output: false
Example 3:

Input: n = 1
Output: true
 
Constraints:

-231 <= n <= 231 - 1
 
Follow up: Could you solve it without loops/recursion?
##################################
           Learnings               
##################################
if number is power of 2 , n & n-1 will always be 0.
power of four will have bit set only in even number of bit position.
'''
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if( (n > 0) and ((n & (n - 1)) == 0) and ((n & 0x55555555) != 0)):
            return True
        else :
            return False
        
if __name__ == '__main__':
  object = Solution()
  print(Solution().isPowerOfFour(16))