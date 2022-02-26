class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1 or n==2:
            return 1
        
        result=0
        first=1
        second=1
        
        for i in range(2,n):
            result=first+second
            first=second
            second=result
        
        return result
