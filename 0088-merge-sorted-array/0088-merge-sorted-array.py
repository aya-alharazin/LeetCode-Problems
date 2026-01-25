class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if n == 0 :
            return nums1
        pointer = len(nums1) - 1
        i = m-1
        j=n-1
        while pointer>=0:
            if nums1[i] > nums2[j]:
                if i < 0 :
                    break
                nums1[pointer] = nums1[i]
                pointer-=1
                i-=1
            else :
                if j < 0:
                    break
                nums1[pointer] =nums2[j]
                pointer-=1
                j-=1
        if i<0:
            nums1[:pointer+1] = nums2[0:j+1]
        print(nums1)
        return nums1

