class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        maxcount=0
        currentcount=0

        for num in nums:
            if num==1:
                currentcount+=1
            else:
                maxcount=max(maxcount,currentcount)
                currentcount=0

        return max(maxcount,currentcount)             
        