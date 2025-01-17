class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        k = len(nums) - k
        while k > 0:
            _ = heapq.heappop(nums)
            k -= 1
        return heapq.heappop(nums)
