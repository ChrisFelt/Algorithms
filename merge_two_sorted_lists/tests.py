import unittest
from merge_two_lists import Solution, ListNode


def create_linked_list(list):
    """
    :param list: List[int]
    :return: ListNode
    """
    if len(list) == 0:
        return None

    # create linked list with values from list
    else:
        head = ListNode()
        cur = head

        # iterate through list
        for i in range(len(list)):
            cur.set_val(list[i])
            if i < len(list) - 1:
                cur.set_next(ListNode())
                cur = cur.get_next()

    return head


def test_solution(head1, head2, answer):
    """
    :param head1: ListNode
    :param head2: ListNode
    :param answer: List[int]
    :return: ListNode, List[bool]
    """
    # generate test solution
    merge_lists = Solution()
    test_head = merge_lists.mergeTwoLists(head1, head2)

    # iterate through solution and check against answer values
    cur_head = test_head
    test_result = []

    i = 0
    while cur_head and i < len(answer) - 1:
        if cur_head.get_val() == answer[i]:
            test_result.append(True)
        else:
            test_result.append(False)

        cur_head = cur_head.get_next()
        i += 1

    return cur_head, test_result


class TestSolution(unittest.TestCase):

    # test the given solutions
    def test_001(self):
        head1 = create_linked_list([1, 2, 4])
        head2 = create_linked_list([1, 3, 4])
        answer = [1, 1, 2, 3, 4, 4]

        cur_head, test_result = test_solution(head1, head2, answer)

        # check that linked list was fully iterated through
        if cur_head:
            self.assertFalse(cur_head.get_next())
        else:
            print("No head found test001")
        # check test_result for any False results
        self.assertFalse(False in test_result)

    def test_002(self):
        head1 = None
        head2 = None
        answer = []

        cur_head, test_result = test_solution(head1, head2, answer)

        # check that linked list was fully iterated through
        if cur_head:
            self.assertFalse(cur_head.get_next())
        else:
            print("No head found test002")  # no head expected for this test
        # check test_result for any False results
        self.assertFalse(False in test_result)

    def test_003(self):
        head1 = None
        head2 = create_linked_list([0])
        answer = [0]

        cur_head, test_result = test_solution(head1, head2, answer)

        # check that linked list was fully iterated through
        if cur_head:
            self.assertFalse(cur_head.get_next())
        else:
            print("No head found test003")
        # check test_result for any False results
        self.assertFalse(False in test_result)

    # test with other node None
    def test_004(self):
        head1 = None
        head2 = create_linked_list([1, 8, 9])
        answer = [1, 8, 9]

        cur_head, test_result = test_solution(head1, head2, answer)

        # check that linked list was fully iterated through
        if cur_head:
            self.assertFalse(cur_head.get_next())
        else:
            print("No head found test004")
        # check test_result for any False results
        self.assertFalse(False in test_result)

    # test negative numbers
    def test_005(self):
        head1 = create_linked_list([-7, -5, 17])
        head2 = create_linked_list([-9, -8, -1])
        answer = [-9, -8, -7, -5, -1, 17]

        cur_head, test_result = test_solution(head1, head2, answer)

        # check that linked list was fully iterated through
        if cur_head:
            self.assertFalse(cur_head.get_next())
        else:
            print("No head found test005")
        # check test_result for any False results
        self.assertFalse(False in test_result)


if __name__ == '__main__':
    unittest.main()
