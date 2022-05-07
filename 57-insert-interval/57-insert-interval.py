class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        results = []
        
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                results.append(newInterval)
                return results + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                results.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
                
        results.append(newInterval)
        return results
        