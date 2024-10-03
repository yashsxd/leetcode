class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = list(magazine)
        for c in ransomNote:
            if c not in magazine:
                return False
            magazine.remove(c)
        return True