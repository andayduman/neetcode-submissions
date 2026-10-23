class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # gonna need to do binary search
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r-l) // 2
            if nums[m] == target:
                return m
            # we need to figure out if m is currently in the rotated half of the list or the non-rotated half
            if nums[l] > nums[m]:
                # in this case, l is in the rotated half and m is in the non-rotated half
                if target > nums[m] and target <= nums[r]:
                    # then target is in the sorted half, so we need to search within this range
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
        return -1