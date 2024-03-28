nums = [0,1,2,2,3,0,4,2]
val = 2

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index +=1
        return index

sol = Solution()
removed_index = sol.removeElement(nums, val)
print("Remaining nums:", nums[:removed_index])
print("val: ", val)