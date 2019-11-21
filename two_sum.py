class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_arr = {}
        for i,num in enumerate(nums):
            left = target-num
            if left not in num_arr:
                num_arr[num] = i
            else:
                return [num_arr[left],i] 
        return []