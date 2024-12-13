class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # time complexity of this solution: O(n), where n is the length of the input string
        sum = 0
        pos = 0

        # sum the following:
        # 26 ** position from end * char_val
        for char in columnTitle[::-1]:
            sum += 26 ** pos * (ord(char) - 64)
            pos += 1

        return sum
    