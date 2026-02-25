class Solution:
    def containsDuplicate(self, a: List[int]) -> bool:
        return len({*a}) < len(a)