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
        pass

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
            while cur_par < len(node_rows[par_row]):
                left = None
                right = None
                # create and connect children to parent if parent exists
                if node_rows[par_row][cur_par] is not None:
                    # child node is created unless the value is None
                    if vals[val_ind] is not None:
                        left = TreeNode(vals[val_ind])
                        node_rows[par_row][cur_par].set_left(left)
                    if vals[val_ind + 1] is not None:
                        right = TreeNode(vals[val_ind + 1])
                        node_rows[par_row][cur_par].set_right(right)
                    val_ind += 2

                # always append children or none to the node_rows array
                node_rows[par_row + 1].append(left)
                node_rows[par_row + 1].append(right)
                cur_par += 1  # left and right child complete, go to next parent

            par_row += 1

        return root
