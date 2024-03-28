nums = [1,2,1]


class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(3):
            for n in nums:
                ans.append(n)
        return ans
    
sol = Solution()
output = sol.getConcatenation(nums)
print(output)