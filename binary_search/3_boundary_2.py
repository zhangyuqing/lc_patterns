# LC 744: https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/

def nextGreatestLetter(letters: list[str], target: str) -> str:
    # first position > target
    left, right = 0, len(letters) - 1
    while left <= right:
        mid = (left + right) // 2
        if letters[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    if left >= len(letters):
        return letters[0]
    else:
        return letters[left]
