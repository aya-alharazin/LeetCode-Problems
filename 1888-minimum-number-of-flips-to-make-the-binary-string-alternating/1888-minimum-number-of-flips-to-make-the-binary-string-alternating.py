class Solution:
    def minFlips(self, s: str) -> int:
        whole_string = s + s
        n = len(s)
 
        start0 = 0
        start1 = 0
        left = 0
        lst = []

        for index in range(len(whole_string)):

            # add current character
            if index % 2 == 0:
                if whole_string[index] == '1':
                    start0 += 1
                else:
                    start1 += 1
            else:
                if whole_string[index] == '1':
                    start1 += 1
                else:
                    start0 += 1

            # remove old character if window > n
            if index - left + 1 > n:
                if left % 2 == 0:
                    if whole_string[left] == '1':
                        start0 -= 1
                    else:
                        start1 -= 1
                else:
                    if whole_string[left] == '1':
                        start1 -= 1
                    else:
                        start0 -= 1
                left += 1

            # one full slide / rotation
            if index - left + 1 == n:
                lst.append(min(start0, start1))

        return min(lst)