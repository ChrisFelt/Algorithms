class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # Time complexity of this solution: O(n^2)
        output = []

        # root node is always 1
        if numRows > 0:
            output.append([1])

        # iterate through rows after the root
        for i in range(1, numRows):
            # first node of the row is always 1
            output.append([1])
            # iterate through remaining  nodes of the row
            for j in range(1, len(output[i - 1])):
                # sum the two parents of the current node
                # parents are always the previous and current element (j) of the previous row
                output[i].append(output[i - 1][j - 1] + output[i - 1][j])

            # last node of the row is always 1
            output[i].append(1)

        return output

