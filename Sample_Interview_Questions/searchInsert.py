class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = len(nums)
        left = 0
        right = l
        mid = (left+right) // 2
        while left<right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                left = mid+1
            elif target < nums[mid]:
                right = mid                
        if nums[mid] == target:
            return mid
        return left
