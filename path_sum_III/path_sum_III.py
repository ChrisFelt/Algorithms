from collections import Counter


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self._val = val
        self._left = left
        self._right = right

    def set_val(self, val):
        self._val = val

    def set_left(self, node):
        self._left = node

    def set_right(self, node):
        self._right = node

    def get_val(self):
        return self._val

    def get_left(self):
        return self._left

    def get_right(self):
        return self._right


class Solution(object):

    def pathSum(self, root, target_sum):
        """
        :param root: TreeNode
        :param target_sum: int
        :rtype: bool
        """
        # Time complexity of this solution: O(n) since memoization is used, all nodes are checked exactly once
        # initialize count memo - the key 0 must have a value of 1 since the target sum is reached
        # when the current branch's running sum = target sum (cur_sum - target_sum = 0)
        count = {0: 1}

        def dfs(node, cur_sum):
            """
            :param node: TreeNode
            :param cur_sum: int
            :rtype: int
            """
            # base case: end of branch reached
            if node is None:
                return 0

            cur_sum += node.get_val()

            # track number of paths that result in target_sum
            # a valid path occurs whenever the key at cur_sum - target_sum exists
            paths = 0 if cur_sum - target_sum not in count else count[cur_sum - target_sum]

            # track number of times the current sum has been reached in this branch
            if cur_sum in count:
                count[cur_sum] += 1
            else:
                count[cur_sum] = 1

            # recurse through children, adding valid paths to the total
            paths += dfs(node.get_left(), cur_sum)
            paths += dfs(node.get_right(), cur_sum)

            # remove the current sum from count when leaving the current branch
            count[cur_sum] -= 1

            return paths  # return total number of paths

        return dfs(root, 0)

    def create_tree(self, vals):
        """
        :param vals: List[int]
        :rtype: TreeNode
        """
        # edge case: empty list passed
        if len(vals) == 0:
            return

        node_rows = []

        # create root node
        root = TreeNode(vals[0])
        node_rows.append([root])

        # track indices
        val_ind = 1
        par_row = 0  # current parent row

        # iterate through values to construct the tree
        while val_ind < len(vals):
            # create a new row in the tree and fill it in
            node_rows.append([])
            cur_par = 0
            while cur_par < len(node_rows[par_row]) and val_ind < len(vals):
                left = None
                right = None
                # create and connect children to parent if parent exists
                if node_rows[par_row][cur_par] is not None:
                    # child node is created unless the value is None
                    if vals[val_ind] is not None:
                        left = TreeNode(vals[val_ind])
                        node_rows[par_row][cur_par].set_left(left)
                    if val_ind + 1 < len(vals) and vals[val_ind + 1] is not None:
                        right = TreeNode(vals[val_ind + 1])
                        node_rows[par_row][cur_par].set_right(right)
                    val_ind += 2

                # always append children or none to the node_rows array
                node_rows[par_row + 1].append(left)
                node_rows[par_row + 1].append(right)
                cur_par += 1  # left and right child complete, go to next parent

            par_row += 1

        return root
