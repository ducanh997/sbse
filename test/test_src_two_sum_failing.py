# Automatically generated by Pynguin.
import src.two_sum as module_0


def test_case_0():
    try:
        str_0 = "`Q'"
        list_0 = [str_0, str_0]
        solution_0 = module_0.Solution(*list_0)
    except BaseException:
        pass


def test_case_1():
    try:
        solution_0 = module_0.Solution()
        solution_1 = module_0.Solution()
        solution_2 = module_0.Solution()
        int_0 = -1445
        int_1 = 818
        int_2 = 874
        int_3 = 1118
        int_4 = 0
        list_0 = [int_1, int_2, int_3, int_4]
        list_1 = solution_2.twoSum(list_0, int_3)
        assert solution_0 is not None
        assert solution_1 is not None
        assert solution_2 is not None
        assert list_1 == [1118, 3]
        list_2 = [int_4, int_0]
        int_5 = -353
        solution_3 = module_0.Solution()
        assert solution_3 is not None
        list_3 = solution_3.twoSum(list_2, int_5)
        assert list_3 is None
        int_6 = 579
        solution_4 = module_0.Solution()
        assert solution_4 is not None
        int_7 = -2508
        int_8 = 50
        solution_5 = module_0.Solution()
        assert solution_5 is not None
        list_4 = [int_6, int_7, int_4, int_8]
        int_9 = -1296
        dict_0 = {}
        solution_6 = module_0.Solution(**dict_0)
        assert solution_6 is not None
        list_5 = solution_6.twoSum(list_4, int_9)
        assert list_5 is None
        bool_0 = False
        float_0 = 0.4
        bytes_0 = b'$E=\xb1\xcd$'
        tuple_0 = bool_0, float_0, bool_0, bytes_0
        list_6 = [int_8, tuple_0, int_4]
        solution_7 = module_0.Solution(*list_6)
    except BaseException:
        pass