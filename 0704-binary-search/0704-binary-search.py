class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarysearch(nums,0,len(nums)-1,target)

    def binarysearch(self,nums,left,right,target):
        if left>right:
            return -1
        mid=left+(right-left)//2

        if nums[mid]==target:
            return mid

        if nums[mid]<target:
            return self.binarysearch(nums,mid+1,right,target)

        return self.binarysearch(nums,left,mid-1,target)             