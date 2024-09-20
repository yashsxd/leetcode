class Solution:
    def shortestPalindrome(self, s: str) -> str:
        prefix, suffix, base = 0, 0, 29
        last_index = 0
        power = 1
        mod = 10**9 + 7

        for i, c in enumerate(s):
            char = ord(c) - ord('a') + 1
            prefix = (prefix * base) % mod
            prefix = (prefix + char) % mod 

            suffix = (suffix + char * power) % mod
            power = (power * base) % mod

            if prefix == suffix:
                last_index = i

        suffix = s[last_index + 1:]
        return suffix[::-1] + s