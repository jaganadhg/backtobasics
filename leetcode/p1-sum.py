class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        processed_nums  = {}
        for n_idx in range(len(nums)):
            if (target-nums[n_idx]) in processed_nums.keys():
                return sorted([n_idx,processed_nums[target-nums[n_idx]]])
            else:
                processed_nums[nums[n_idx]] = n_idx


