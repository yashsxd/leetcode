class ProductOfNumbers:

    def __init__(self):
        self.product = []
        self.val = 1

    def add(self, num: int) -> None:
        if num == 0:
            self.product = []
            self.val = 1
        else:
            self.val *= num
            self.product.append(self.val)

    def getProduct(self, k: int) -> int:
        if len(self.product) < k:
            return 0
        if len(self.product) == k:
            return self.val
        return self.product[-1] // self.product[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)