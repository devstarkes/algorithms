class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.canJump2(nums)
        # return self.canJampFrom(0, nums)

    def canJampFrom(self, position, nums):
        if position >= len(nums) - 1:
            return True

        for next_position in range(position + 1, position + 1 + nums[position]):
            if self.canJampFrom(next_position, nums):
                return True

        return False
    
    def canJump2(self, nums):
        last_index_position = len(nums) - 1

        for i in reversed(range(0, len(nums) - 1)):
            print(i, nums[i])

            if i + nums[i] >= last_index_position:
                last_index_position = i
            
            print(last_index_position)
        
        return last_index_position == 0
