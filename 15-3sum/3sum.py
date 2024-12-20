class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        n, p, z = [], [], []
        for num in nums:
            if num > 0: p.append(num)
            elif num < 0: n.append(num)
            else: z.append(num)
        
        N, P = set(n), set(p)
        if z:
            for num in P:
                if -1 * num in N:
                    ans.add((-1 * num, 0, num))

        if len(z) >= 3:
            ans.add((0,0,0))
        
        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                target = -1 * (n[i] + n[j])
                if target in P:
                    ans.add(tuple(sorted([n[i], n[j], target])))
        
        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                target = -1 * (p[i] + p[j])
                if target in N:
                    ans.add(tuple(sorted([p[i], p[j], target])))
        return list(ans)