class MyCalendarTwo:

    def __init__(self):
        self.overlapping = []
        self.non_overlapping = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlapping:
            if s < end and start < e:
                return False

        for s, e in self.non_overlapping:
            if s < end and start < e:
                self.overlapping.append((max(start, s), min(end, e)))
        
        self.non_overlapping.append((start, end))
        return True


        self.calendar.add((start, 1))
        self.calendar.add((end, -1))

        total = 0
        for i, j in self.calendar:
            total += j

            if total == 3:
                self.calendar.remove((start, 1))
                self.calendar.remove((end, -1))
                return False
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)