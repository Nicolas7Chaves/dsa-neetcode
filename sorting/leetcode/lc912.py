class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            j = i -1
            #we make j = i - 1 since were starting i at 1 
            while j >= 0 and nums[j+ 1] < nums[j]:
                tmp = nums[j + 1]
                nums[j+1] = nums[j]
                nums[j] = tmp
                j -= 1
        return nums