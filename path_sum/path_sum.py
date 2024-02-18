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
    def has_path_sum(self, root, target_sum):
        """
        :type root: TreeNode
        :type target_sum: int
        :rtype: bool
        """
        pass
        # recursively search down each branching path to find the solution - return True if target reached, else None

    def tree_recurse(self, cur, node_list, left_ind=1, right_ind=2):
        # base case 1: left index exceeds the node list
        if left_ind >= len(node_list):
            return

        # recurse down left child path
        if node_list[left_ind] is not None:
            # find next indices for children of left node
            # next left child index: always add right_ind to left_ind
            # next right child index: always add + 1 to left_ind
            next_left_ind = left_ind + right_ind
            next_right_ind = next_left_ind + 1
            cur.set_left(TreeNode(node_list[left_ind]))
            self.tree_recurse(cur.get_left(), node_list, next_left_ind, next_right_ind)

        # base case 2: right index exceeds the node list
        if right_ind >= len(node_list):
            return

        # recurse down right child path
        if node_list[right_ind] is not None:
            # find next indices for children of right node
            next_left_ind = (2 * right_ind) + left_ind
            next_right_ind = next_left_ind + 1
            cur.set_right(TreeNode(node_list[right_ind]))
            self.tree_recurse(cur.get_right(), node_list, next_left_ind, next_right_ind)

    def gen_tree(self, node_list):
        """
        :param node_list: List[int], breadth-first ordered list of tree node values
        :return: TreeNode
        """
        # edge case: empty list passed
        if len(node_list) == 0:
            return

        # create root node and generate tree
        root = TreeNode(node_list[0])

        self.tree_recurse(root, node_list)
        return root


