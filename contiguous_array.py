class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maximum = 0
        count = 0
        counts = {0: -1}
        
        for i, n in enumerate(nums):
            count = count + 1 if n else count - 1
            
            if count in counts:
                maximum = max(maximum, i - counts[count])
            else:
                counts[count] = i

        return maximum
