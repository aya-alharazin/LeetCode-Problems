class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        list = []
        for i in range(len(nums)+1):
            list.append(0)
        for x in nums:
            list[x] = 1
        for i in range( 1 , len(list)):
            if list[i] == 0:
                result.append(i)
        return result
