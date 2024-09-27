class MyCalendarTwo:

    def __init__(self):
        self.overlapping = []
        self.non_overlapping = []

    def book(self, start: int, end: int) -> bool:
        
        for s, e in self.overlapping:
            if start < e and end > s:
                return False

        for s, e in self.non_overlapping:        
            if start < e and end > s:
                self.overlapping.append((max(start, s), min(end, e)))
        self.non_overlapping.append((start, end))

        return True
        



# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)