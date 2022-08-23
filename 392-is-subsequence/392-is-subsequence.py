class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) == 0:
            return True
        elif len(t) == 0:
            return False
        
        pointer1 = 0

        for i in range(len(t)):
            if s[pointer1] == t[i]:
                pointer1 += 1
                if pointer1 == len(s):
                    return True
        return False
    