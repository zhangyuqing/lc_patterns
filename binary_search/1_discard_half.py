# LC 162: https://leetcode.com/problems/find-peak-element/description/

from typing import List

def findPeakElement(nums: List[int]) -> int:
    if len(nums) == 1:
        return 0
    
    if nums[0] > nums[1]:
        return 0
    elif nums[-1] > nums[-2]:
        return len(nums) - 1
    
    left, right = 1, len(nums) - 2
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            # based on gradient flow of the array, 
            # there must exist a peak on the right, 
            # so discard left
            left = mid + 1
        elif nums[mid] < nums[mid - 1]:
            right = mid - 1
        else:
            return mid
