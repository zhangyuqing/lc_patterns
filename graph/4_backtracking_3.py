# LC 78: https://leetcode.com/problems/subsets/description/

def subsets(nums: list[int]) -> list[list[int]]:
    output = []
    
    def backtrack(prev_set, idx):
        # idx - already made all include/exclude decisions ending at idx-1, considering idx
        if idx == len(nums):
            output.append(prev_set.copy())
        else:
            prev_set.append(nums[idx])
            backtrack(prev_set, idx+1)
            prev_set.pop()

            backtrack(prev_set, idx+1)
        
    backtrack([], 0)
    return output

