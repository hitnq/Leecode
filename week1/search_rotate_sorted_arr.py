class Solution(object):
    def bisearch(self,nums,low,high,target):
        if low > high:
            return -1
        mid = (low+high)/2
        if nums[mid]==target:
            return mid
        if nums[mid] < nums[high]:#说明右边是有序数组
            if nums[mid] < target and target <=nums[high]:
                return self.bisearch(nums,mid+1,high,target)
            else:
                return self.bisearch(nums,low,mid-1,target)
        else:#说明左边是有序数组
            if nums[mid] > target and nums[low] <= target:
                return self.bisearch(nums,low,mid-1,target)
            else:
                return self.bisearch(nums,mid+1,high,target)
        
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.bisearch(nums,0,len(nums)-1,target)