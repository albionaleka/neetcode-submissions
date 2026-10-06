class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        removed = ''.join(c for c in s if c.isalnum())
        string = list(removed)

        return string == string[::-1]
        