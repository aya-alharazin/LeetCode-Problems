class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==1:
            return x
        if n == 0 :
            return 1
        if n < 0 : 
            n = -n
            result = self.myPow(x, n // 2)
            if n%2 != 0:
                return 1 / (result*result*x)
            return 1/(result*result)
        else :
            result = self.myPow(x, n // 2)
            if n%2 != 0:
                return result*result*x
            return result*result

