class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return sum(derived) & 1 == 0