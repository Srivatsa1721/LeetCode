class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = ''.join([char for char in s if char.isalnum()]).lower()
        if p ==p [::-1]:
            return True
        else:
            return False
        

