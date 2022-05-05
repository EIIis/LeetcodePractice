class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Sort our input
        nums.sort()
        # Initalize list where we will return our results
        res = []
        
        # Iterating through our list from 1 through len(nums) -2
        for i in range(len(nums) - 2):
            # Left pointer
            left = i + 1
            # Right pointer
            right = len(nums) - 1
            # We go until our two pointers meet each outher
            while left < right:
                # Adding up our current numbers that we're on to see what they add up to
                currentVal = nums[i] + nums[left] + nums[right]
                # Simplify the array incase we need to append. Cleaner code, not needed
                triplets = [nums[i], nums[left], nums[right]]
                # Checking if the current number equals to 0
                if currentVal == 0:
                    # Checking to see if duplicates exist or not. Regardless we move both pointers to there respective location
                    if triplets not in res:
                        res.append(triplets)
                        left += 1
                        right -= 1
                    else:
                        left += 1
                        right -= 1
                        continue
                # If the triplets total val is less then 0, we'll increase the total by moving the left pointer to the right
                elif currentVal < 0:
                    left += 1
                    # If the triplets total val is greater then 0, we'll decrease the total by moving the right pointer to the left
                elif currentVal > 0:
                    right -= 1
        
        return res
                