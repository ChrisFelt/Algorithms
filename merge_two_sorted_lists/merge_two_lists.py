# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self._val = val
        self._next = next

    def get_val(self):
        return self._val

    def get_next(self):
        return self._next

    def set_val(self, val):
        self._val = val

    def set_next(self, node):
        self._next = node


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: ListNode
        :type list2: ListNode
        :return: ListNode
        """
        # Time Complexity of this solution: O(n + m)
        # create head of return linked list
        head = ListNode()
        cur_node = head

        # iterate through list1: O(n) complexity
        # either node passed into the function could be None, so we will iterate through each separately
        while list1:
            # check if list2 has ended
            if list2 is None:
                cur_node, list1 = self.update_node(cur_node, list1)
            
            # compare current nodes from list1 and list2 and assign lowest value to cur_node   
            else:
                # update current node with next lowest value
                if list1.get_val() > list2.get_val():
                    cur_node, list2 = self.update_node(cur_node, list2)

                else:
                    cur_node, list1 = self.update_node(cur_node, list1)

        # iterate through remaining nodes of list2, if any: O(m) complexity
        while list2:
            cur_node, list2 = self.update_node(cur_node, list2)

        return head.get_next()

    def update_node(self, cur_node, list_node):
        """
        :type cur_node: ListNode
        :type list_node: ListNode
        :return: List[ListNode, ListNode]
        """
        cur_node.set_next(list_node)
        return cur_node.get_next(), list_node.get_next()
                