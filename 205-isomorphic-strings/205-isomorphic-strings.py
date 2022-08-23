class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Checking to see if they're the same length
        if len(s) != len(t):
            return False
        else:
            # Doing mapping solution, the key will be the letter that we're iterating
            # and the key will be the letter that it's matched to. 
            map1 = {}
            map2 = {}
            
            for r, l in zip(s, t):
                if r not in map1 and l not in map2:
                    map1[r] = l
                    map2[l] = r
                elif map1.get(r) != l or map2.get(l) != r:
                    return False
        return True