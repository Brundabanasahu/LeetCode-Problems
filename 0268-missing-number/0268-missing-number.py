class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        actual=0
        n=len(nums)
        excepted=n*(n+1)//2

        for num in nums:
            actual+=num

        return excepted-actual
