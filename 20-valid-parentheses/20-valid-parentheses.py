class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Initalizing our stack
        stack = []
        
        # Checking element of the string to determine next step
        # Adding to the stack if it's the correct element
        for char in s:
            if char == "{" or char == "[" or char == "(":
                stack.append(char)
        # If it a closing bracket, we check that it's valid
            elif char == "}":
                if len(stack) == 0:
                    return False
                elif stack[-1] != "{":
                    return False
                stack.pop(-1)
            elif char == "]":
                if len(stack) == 0:
                    return False
                elif stack[-1] != "[":
                    return False
                stack.pop(-1)
            elif char == ")":
                if len(stack) == 0:
                    return False
                elif stack[-1] != "(":
                    return False
                stack.pop(-1)
                
        # Once we go through the entire string, checking to see if we have any elements left in the stack
        if len(stack) != 0:
            return False
        return True
    