# LC 34: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

from typing import List

def searchRange(nums: List[int], target: int) -> List[int]:
    output = [-1, -1]
    if len(nums) == 0:
        return output

    left1, right1 = 0, len(nums) - 1
    while left1 <= right1:
        mid1 = (left1 + right1) // 2
        if nums[mid1] >= target:
            right1 = mid1 - 1
        else:
            left1 = mid1 + 1
    if left1 == len(nums) or (left1 < len(nums) and nums[left1] != target):
        return output
    else:
        output[0] = left1

    left2, right2 = 0, len(nums) - 1
    while left2 <= right2:
        mid2 = (left2 + right2) // 2
        if nums[mid2] <= target:
            left2 = mid2 + 1
        else:
            right2 = mid2 - 1
    output[1] = right2
    return output

