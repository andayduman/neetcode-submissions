class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        # performing binary search
        l, r = 0, len(nums) - 1
        while l <= r:
            # If the subarray is already sorted, nums[l] is the smallest
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break
                
            m = l + ((r - l) // 2)
            res = min(res, nums[m])

            if nums[m] >= nums[l]:
                # if our midpoint is within the rotated part of the array, we scan the other part
                # so we scan the right side
                l = m + 1
            else:
                r = m - 1
        return res