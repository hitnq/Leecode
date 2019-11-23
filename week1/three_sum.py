class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        k = 0
        for k,num in enumerate(nums):
            if k == 0 or nums[k]>nums[k-1]:
                i = k+1
                j = len(nums)-1
                while i < j:
                    left = 0-num
                    if nums[i] + nums[j] == left:
                        res.append([nums[index] for index in [i,j,k]])
                        i += 1
                        j -= 1
                        while i < j and nums[i] == nums[i-1]:
                            i += 1
                        while i < j and nums[j] == nums[j+1]:
                            j -= 1
                    elif nums[i] + nums[j] < left:
                        i += 1
                    elif nums[i] + nums[j] > left:
                        j -= 1
        return res