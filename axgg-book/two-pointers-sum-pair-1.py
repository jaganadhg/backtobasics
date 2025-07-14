from typing import List

"""
Givn a list of numbers and target find the pair that sum up
to the target using two pointers technique.
[-5, -2, 3, 4, 6] target = 7 output = [2,3]
"""


def pair_sum_naive_approch(nums: List[int], target: int) -> List[int]:
    """
    Naive approach to find the pair that sums up to the target.
    Time complexity: O(n^2)
    Space complexity: O(1)
    Args:
        nums (List[int]): List of integers.
        target (int): Target sum.
    Returns:
        List[int]: Pair of numbers that sum up to the target.
    """

    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def pair_sum_two_pointers(nums: List[int], target: int) -> List[int]:
    """
    Two pointers approach to find the pair that sums up to the target.
    Time complexity: O(n)
    Space complexity: O(1)
    Args:
        nums (List[int]): List of integers.
        target (int): Target sum.
    Returns:
        List[int]: Pair of numbers that sum up to the target.
    """
    nums.sort()
    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []


if __name__ == "__main__":
    nums = [-5, -2, 3, 4, 6]
    target = 7
    print(pair_sum_naive_approch(nums, target))
    print(pair_sum_two_pointers(nums, target))
