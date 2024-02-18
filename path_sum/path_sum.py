# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
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

    def gen_tree(self, node_list):
        """
        :param node_list: List[int], breadth-first ordered list of tree node values
        :return: TreeNode
        """
        pass
