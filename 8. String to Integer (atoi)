class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        sign = -1 if s[0] == '-' else 1
        is_sign = False
        res = ''
        for i in s:
            if i == '-' or i == '+':
                if is_sign or s.index(i) != 0:
                    break
                is_sign = True
            if i.isdigit():
                res += i
            elif i not in '+-':
                break
        if res == '':
            return 0
        n = int(res) * sign
        if  n > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif n < -2 ** 31:
            return -2 ** 31
        return n
