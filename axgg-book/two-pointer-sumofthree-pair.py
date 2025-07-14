from typing import List

"""
Give a list of numbers and target, fid all the 
triplets that sum up to the target without duplicates

[0, -1, 2, -3, 1] target = 0 output = [[-3, 1, 2], [-1, 0, 1]]
"""


def n_sum_triplets(nums: List[int], target: int) -> List[List[int]]:
    """
    Find all unique triplets in the list that sum up to the target.
    Time complexity: O(n^2)
    Space complexity: O(1)
    Args:
        nums (List[int]): List of integers.
        target (int): Target sum.numes
    Returns:
        List[List[int]]: List of unique triplets that sum up to the target.
    """
    nums.sort()

    triplets = list()

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == target:
                    triplet = [nums[i], nums[j], nums[k]]
                    if triplet not in triplets:
                        triplets.append(triplet)

    return triplets


def pair_sum_tp_approach(nums: List[int], start: int, target: int) -> List[int]:
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
    left, right = start, len(nums) - 1

    pairs = list()

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            pairs.append([nums[left], nums[right]])
            left += 1
            while left < right and nums[left] == nums[left - 1]:
                left += 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return pairs


def triple_sum_with_two_pointers(nums: List[int], target: int) -> List[List[int]]:
    """
    Find all unique triplets in the list that sum up to the target using two pointers.

    Args:
        nums (List[int]): List of integers.
        target (int): Target sum.

    Returns:
        List[List[int]]: List of unique triplets that sum up to the target.
    """
    nums.sort()
    triplets = []

    for i in range(len(nums)):
        if nums[i] == 0:
            break  # Skip if the first number is zero
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        pairs = pair_sum_tp_approach(nums, i + 1, -nums[i])

        for pair in pairs:
            triplet = [nums[i]] + pair
            if triplet not in triplets:
                triplets.append(triplet)

    return triplets


if __name__ == "__main__":
    nums = [0, -1, 2, -3, 1]
    target = 0
    print(n_sum_triplets(nums, target))
    print(triple_sum_with_two_pointers(nums, target))
