nums = [0,0,1,1,1,2,2,3,3,4]


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)


sol = Solution()
sol.removeDuplicates(nums)
print("Remaining nums:", nums)