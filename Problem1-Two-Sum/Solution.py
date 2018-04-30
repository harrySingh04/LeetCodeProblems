class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        myDict = {}
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in myDict:
                return [myDict.get(diff),i]
            else:
                myDict[nums[i]]=i
        #print(myDict)
        return []

## Time-Complexity is O(n) where n is number of elements in the nums array
