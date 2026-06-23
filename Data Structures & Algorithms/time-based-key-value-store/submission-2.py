class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""

        l,r = 0, len(self.data[key])
        while l < r:
            mid = (l + r) // 2
            if self.data[key][mid][1] > timestamp:
                r = mid
            else:
                l = mid + 1
        
        return self.data[key][r-1][0] if r != 0 else ""
