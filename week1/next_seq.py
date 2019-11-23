class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)<2:
            return 
        l = -1
        r = -1
        for i in range(len(nums)-1,-1,-1):
            if nums[i] > nums[i-1]:
                l = i-1
                r = i
                break
        b = len(nums)-1
        while r < b:
            nums[r],nums[b] = nums[b],nums[r]
            r += 1
            b -= 1
        for k in range(l+1,len(nums)):
            if nums[k] > nums[l]:
                nums[k],nums[l] = nums[l],nums[k]
                break