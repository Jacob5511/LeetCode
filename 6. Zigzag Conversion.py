class Solution:
    def convert(self, s: str, numRows: int) -> str:
        current_row = 0
        row = numRows
        sp = ['' for _ in range(row)]
        is_down = False
        if row == 1:
            return s
        for char in s:
            sp[current_row] += char

            if current_row == 0 or current_row == row - 1:
                is_down = not is_down

            current_row += 1 if is_down else -1
        return ''.join(sp)
