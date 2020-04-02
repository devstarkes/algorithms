class Solution:
    def isHappy(self, n: int) -> bool:
        slow = self.step(n)
        fast = self.step(slow)

        while (fast != 1):
            if (slow == fast):
                return False
            else:
                slow = self.step(slow)
                fast = self.step(self.step(fast))
        return True
        
    def step(self, n):
        result = 0

        while n:
            result += pow(n % 10, 2)
            n = n // 10

        return result
