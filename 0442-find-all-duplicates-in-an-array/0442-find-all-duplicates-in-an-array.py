class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dict = {}

        for x in nums:
            dict[x] = dict.get(x, 0) +1
        list = []
        for key , value in dict.items():
            if value > 1:
                list.append(key)
        return list
        