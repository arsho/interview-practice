
def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 1
        c = 0
        while n > 1:
            c += 1
            n -= 2
            p = c + n
            a, b = 1, 1
            for i in range(n + 1, p+1):
                a *= i
            for i in range(2, c+1):
                b *= i
            x += (a // b)
return x
