from typing import List


class PowerSet:
    def generate_subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 0:
            return [[]]

        subsets = []

        def backtrack(current_index, current_subset):
            # base case
            if current_index >= len(nums):
                temp_subset = [num for num in current_subset]
                subsets.append(temp_subset)
                return

            # take the current element
            current_subset.append(nums[current_index])
            backtrack(current_index + 1, current_subset)

            # leave the current element
            current_subset.pop()
            backtrack(current_index+1, current_subset)

        backtrack(0, [])
        return subsets


test = PowerSet()
print(test.generate_subsets([2, 4, 6, 8]))
