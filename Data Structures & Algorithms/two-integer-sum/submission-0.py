class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}        
        for i, i_val in enumerate(nums):
            diff = target - i_val
            j = seen.get(diff)
            if j is not None and i != j:
                return [j, i]
            seen[i_val] = i
