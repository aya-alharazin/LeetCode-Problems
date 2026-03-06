class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        is_zero_seen = False
        is_one_after_zero_seen = False
        for x in s :
            if x == '0':
                is_zero_seen = True
            if is_zero_seen and x == '1':
                return False
        return True
