class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        ans = int(str(abs(x))[::-1])
        if ans >= 2147483647: return 0
        return ans if x > 0 else -ans
