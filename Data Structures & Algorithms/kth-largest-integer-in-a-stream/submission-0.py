class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k_val = k
        self.nums_arr = nums

    def add(self, val: int) -> int:
        self.nums_arr.append(val)
        sorted_nums = sorted(self.nums_arr)
        len_nums = len(sorted_nums)
        kth_largest_idx = len_nums - self.k_val
        return sorted_nums[kth_largest_idx]
