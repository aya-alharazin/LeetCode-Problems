class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        power = 2 ** n
        lst = [i for i in range (power)]
        for i in range(power):
            binary = format(i, f'0{n}b') 
            if binary not in nums :
                return binary