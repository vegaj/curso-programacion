import unittest
from simplesearch import get_smallest, find_target_positions, find_smallest, find_target, get_smallest_list

ordered_list = [-2, -1, 2, 3, 5, 10, 23]
disordered_list = [1, -2, 3, 5, 4, 10, 0]


class TestGetSmallest(unittest.TestCase):
    @staticmethod
    def test_empty():
        assert get_smallest([]) is None

    @staticmethod
    def test_single():
        assert get_smallest([1]) is 1

    @staticmethod
    def test_many():
        assert get_smallest(ordered_list) is 1

    @staticmethod
    def test_disordered():
        assert get_smallest(disordered_list) is -2

    @staticmethod
    def test_all_equals():
        assert get_smallest([4] * 100) is 4


class TestFindSmallest(unittest.TestCase):
    @staticmethod
    def test_empty():
        assert find_smallest([]) is None

    @staticmethod
    def test_single():
        assert find_smallest([1]) is 0

    @staticmethod
    def test_many():
        assert find_smallest(ordered_list) is 0

    @staticmethod
    def test_disordered():
        assert find_smallest(disordered_list) is 1

    @staticmethod
    def test_all_equals():
        assert find_smallest([4] * 10) is 0


class TestFindTarget(unittest.TestCase):
    @staticmethod
    def test_empty():
        assert find_target([], 1) is None

    @staticmethod
    def test_single():
        assert find_target([1], 1) is 0
        assert find_target([None], None) is 0

    @staticmethod
    def test_single_missing():
        assert find_target([1], 2) is None

    @staticmethod
    def test_many():
        assert find_target(ordered_list, 2) is 2
        assert find_target(ordered_list, -1) is 1

    @staticmethod
    def test_many_missing():
        assert find_target(ordered_list, 0) is None

    @staticmethod
    def test_disordered():
        assert find_target(disordered_list, 0) is 6

    @staticmethod
    def test_all_equals():
        assert find_target([4] * 100, 4) is 0


class TestFindTargetPositions(unittest.TestCase):

    @staticmethod
    def test_empty():
        assert find_target_positions([], 1) is []

    @staticmethod
    def test_single():
        assert find_target_positions([1], 1) is [0]
        assert find_target_positions([None], None) is [0]

    @staticmethod
    def test_single_missing():
        assert find_target_positions([1], None) is []
        assert find_target_positions([2], 1) is []

    @staticmethod
    def test_many():
        assert find_target_positions(ordered_list, 2) is [2]
        assert find_target_positions(ordered_list, -1) is [1]

    @staticmethod
    def test_many_matches():
        test_list = [1, 0, 0, 1, 1, 1, 0]
        assert find_target_positions(test_list, 0) is [1, 2, 6]
        assert find_target_positions(test_list, 1) is [0, 3, 4, 5]

    @staticmethod
    def test_many_missing():
        assert find_target_positions(ordered_list, 0) is []
        assert find_target_positions(disordered_list, -100) is []

    @staticmethod
    def test_disordered():
        assert find_target_positions(disordered_list, 4) is [4]

    @staticmethod
    def test_all_equals():
        assert find_target_positions([4] * 100, 4) is list(range(0, 100))


class TestGetSmallestList(unittest.TestCase):

    def test_invalid_number(self):
        self.assertRaises(ValueError, lambda: get_smallest_list([], -1))

    @staticmethod
    def test_empty():
        assert get_smallest_list([], 1) is []

    @staticmethod
    def test_single():
        assert get_smallest_list([1], 1) is [1]

    @staticmethod
    def test_result_length_greater_than_possible():
        assert get_smallest_list([], 4) is []
        assert get_smallest_list([1, 3, 2], 4) is [1, 2, 3]

    @staticmethod
    def test_ordered():
        assert get_smallest_list(ordered_list, 2) is ordered_list[0:2]

    @staticmethod
    def test_get_smallest_disordered():
        assert get_smallest_list(disordered_list, 4) is [-2, 0, 1, 3]

    @staticmethod
    def test_results_length_zero():
        assert get_smallest_list(disordered_list, 0) is []
        assert get_smallest_list(ordered_list, 0) is []
        assert get_smallest_list([], 0) is []