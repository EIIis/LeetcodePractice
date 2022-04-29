class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        storedNum = {} # Hashmap to store index and numbers
        
        for i, num  in enumerate(nums): # Iterating through nums grabbing index and nums
            result = target - num # Finding number we need
            if result in storedNum: # Checking if the number we need exist
                return [i, storedNum[result]] # If it is, we return the indexs
            else: # If not..
                storedNum[num] = i # WE add that number to the hashmap
        return [] # Going through the array, noo solution we return empty array as results