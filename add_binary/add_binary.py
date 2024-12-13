class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # time complexity of this solution: O(n)
        sum = []
        a_ind = len(a) - 1
        b_ind = len(b) - 1

        carry = 0

        # iterate through a and b
        while a_ind >= 0 or b_ind >= 0 or carry == 1:
            if a_ind >= 0:
                # carry goes up one if value at current index is 1 
                carry += int(a[a_ind])
                a_ind -= 1
            
            if b_ind >= 0:
                carry += int(b[b_ind])
                b_ind -= 1
            
            # carry % 2 = result of the current position
            # even when both a and b are 1 and carry is 1, since 3%2 = 1
            sum.append(str(carry % 2))
            # find value of carry for next highest position
            carry = carry // 2
        
        result = sum[::-1] # reverse sum
        # join operation joins an iteratable to the string
        return "".join(result)