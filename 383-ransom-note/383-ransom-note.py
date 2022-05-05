class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # Initalize dictionary to store letters in magazine
        magMap = {}
        # Pass through magaize and add all letter of magazine to dictionary
        for letter in magazine:
            if letter not in magMap:
                magMap[letter] = 1
            else:
                magMap[letter] += 1
                

        # Pass through ransomeNote to check if letters in ransomeNote exist in magazine
        for letter in ransomNote:
            # If letter doesn't exist in our dict the we can stop and return false
            if letter not in magMap:
                return False
            else:
                # If letter does exist we decrease the value of the key by 1
                magMap[letter] -= 1
                # We then check if the key's value is 0, if it is then we delete
                if magMap.get(letter) == 0:
                    del magMap[letter]  
        return True
                