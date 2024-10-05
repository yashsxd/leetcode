class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        counter, n = Counter(s1), len(s1)

        for i in range(len(s2)):
            if s2[i] in counter: counter[s2[i]] -= 1
            if i >= n and s2[i-n] in counter: counter[s2[i-n]] += 1

            if all([counter[i] == 0 for i in counter]):
                return True
        return False