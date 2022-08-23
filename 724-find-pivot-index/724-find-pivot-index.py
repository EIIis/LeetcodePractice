class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right = sum(nums)
        left = 0
        
        for i in range(len(nums)):
            right -= nums[i]
            if right == left:
                return i
            else:
                left += nums[i]
        return -1
        