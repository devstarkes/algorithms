class Solution:
    def reverse(self, x: int) -> int:
        if not x:
            return 0
        
        pointer = 1 if x > 0 else -1
        result = 0
        x = abs(x)

        while x:
            tmp = x % 10
            result = result * 10 + tmp
            x = x // 10
            
        result = result * pointer

        if result < (-2 ** 31) or result > 2 ** 31 - 1:
            return 0
    
        return result
