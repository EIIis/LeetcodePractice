class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = 0
        res = []
        
        for num in nums:
            count += num
            res.append(count)
        return res
    