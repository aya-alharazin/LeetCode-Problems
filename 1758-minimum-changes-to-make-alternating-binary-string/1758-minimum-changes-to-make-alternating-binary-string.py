class Solution:
    def minOperations(self, s: str) -> int:
        start0 = 0
        start1 = 0
        # loop over even positions
        for i in range(0,len(s),2):
            if s[i] == '1':
                start0+=1
            else :
                start1+=1
        # loop over odd positions
        for i in range(1,len(s),2):
            if s[i] == '1':
                start1+=1
            else :
                start0+=1
        return min(start0,start1)