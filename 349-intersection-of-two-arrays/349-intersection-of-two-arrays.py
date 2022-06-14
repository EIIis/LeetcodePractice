class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        allNums = set()
        
        for nums in nums1:
            if nums not in allNums:
                allNums.add(nums)
        result = []
        for nums in nums2:
            if nums in allNums:
                if nums not in result:
                    result.append(nums)
        
        return result
        