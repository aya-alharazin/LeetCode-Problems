class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        whole_string = s + s

        flip0 = 0   # mismatches with pattern 010101...
        flip1 = 0   # mismatches with pattern 101010...

        left = 0
        result = float('inf')

        for right in range(len(whole_string)):

            # expected characters
            if right % 2 == 0:
                expected0 = '0'
                expected1 = '1'
            else:
                expected0 = '1'
                expected1 = '0'

            # add new character
            if whole_string[right] != expected0:
                flip0 += 1
            if whole_string[right] != expected1:
                flip1 += 1

            # shrink window if it becomes larger than n
            if right - left + 1 > n:

                if left % 2 == 0:
                    expected0 = '0'
                    expected1 = '1'
                else:
                    expected0 = '1'
                    expected1 = '0'

                if whole_string[left] != expected0:
                    flip0 -= 1
                if whole_string[left] != expected1:
                    flip1 -= 1

                left += 1

            # when window size = n → valid rotation
            if right - left + 1 == n:
                result = min(result, flip0, flip1)

        return result