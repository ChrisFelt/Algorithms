class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # very fast solution with relatively high memory usage
        # time complexity for this answer is O(n)
        dlen = len(digits)

        if dlen == 0:
            return digits

        if digits[dlen - 1] == 9:
            # add one to each element starting with last
            for i in range(dlen - 1, -1, -1):
                if digits[i] == 9:
                    digits[i] = 0
                    # add an element to list if leading digit is 9
                    if i == 0:
                        digits.append(0)
                        # shift digits one to the right
                        for j in range(dlen, -1, -1):
                            if j == 0:
                                # leading digit is a 1
                                digits[j] = 1
                                return digits
                            else:
                                digits[j] = digits[j - 1]
                else:
                    digits[i] += 1
                    return digits

        else:
            digits[dlen - 1] += 1
            return digits
        