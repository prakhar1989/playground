class Solution:
    # @param {integer} num
    # @return {integer}
    def addDigits(self, num):
        if len(str(num)) == 1:
            return num
        return self.addDigits(sum(map(int, str(num))))

    # non recursive solution
    def addDigits(self, num):
        if num == 0:
            return 0
        return 9 if num % 9 == 0 else num % 9
