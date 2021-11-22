class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        def helper(s, left, right):
            if left > right: return
            s[left], s[right] = s[right], s[left]
            return helper(s, left+1, right-1)
        helper(s, 0, len(s)-1)
