class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        summ=0
        minlength=float('inf')
        for right in range(len(nums)):
            summ+=nums[right]

            while summ>=target:
                minlength=min(minlength,right-left+1)
                summ-=nums[left]
                left+=1
        return 0 if minlength==float('inf') else minlength        
        