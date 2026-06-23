class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is smaller for efficiency
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total_left_size = (m + n + 1) // 2
        
        # Binary search on how many elements to take from nums1 for left partition
        min_from_nums1, max_from_nums1 = 0, m
        
        while min_from_nums1 <= max_from_nums1:
            nums1_left_count = (min_from_nums1 + max_from_nums1) // 2
            nums2_left_count = total_left_size - nums1_left_count
            
            # Get boundary elements (last of left partitions, first of right partitions)
            nums1_left_max = nums1[nums1_left_count - 1] if nums1_left_count > 0 else float('-inf')
            nums2_left_max = nums2[nums2_left_count - 1] if nums2_left_count > 0 else float('-inf')
            nums1_right_min = nums1[nums1_left_count] if nums1_left_count < m else float('inf')
            nums2_right_min = nums2[nums2_left_count] if nums2_left_count < n else float('inf')
            
            # Check if partition is valid (left partition max ≤ right partition min)
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                if (m + n) % 2 == 0:
                    left_partition_max = max(nums1_left_max, nums2_left_max)
                    right_partition_min = min(nums1_right_min, nums2_right_min)
                    return (left_partition_max + right_partition_min) / 2
                else:
                    return max(nums1_left_max, nums2_left_max)
            
            elif nums1_left_max > nums2_right_min:
                # Too many from nums1 in left partition
                max_from_nums1 = nums1_left_count - 1
            else:
                # Too few from nums1 in left partition
                min_from_nums1 = nums1_left_count + 1