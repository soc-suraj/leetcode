'''
File:  reverse-words-in-a-string-iii.py
##################################
           Question               
##################################
  Problem statement 
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "Mr Ding"
Output: "rM gniD"
 

Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
##################################
           Learnings               
##################################
  To reverse string in python s = s[::-1]
           
'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = s.split(' ')
        for i in range(len(s_list)):
            s_list[i] = s_list[i][::-1]
        s = " ".join(s_list)
        return s
    
if __name__ == '__main__':
  object = Solution()
  print(Solution().reverseWords("Let's take LeetCode contest"))