# Automatically generated by Pynguin.
import src.container_water as module_0


def test_case_0():
    try:
        int_0 = None
        dict_0 = {int_0: int_0, int_0: int_0, int_0: int_0}
        int_1 = -2489
        list_0 = [int_1]
        solution_0 = module_0.Solution()
        int_2 = solution_0.maxArea(list_0)
        assert int_2 == 0
        assert solution_0 is not None
        list_1 = [dict_0, dict_0, dict_0]
        solution_1 = module_0.Solution(*list_1)
    except BaseException:
        pass


def test_case_1():
    try:
        int_0 = -825
        solution_0 = module_0.Solution()
        int_1 = 11
        list_0 = [int_0, int_0, int_0, int_1]
        solution_1 = module_0.Solution()
        int_2 = solution_1.maxArea(list_0)
        assert int_2 == 0
        assert solution_0 is not None
        assert solution_1 is not None
        str_0 = '<o\x0ce4?,Z0Ot1N\x0b'
        solution_2 = module_0.Solution()
        assert solution_2 is not None
        dict_0 = {str_0: str_0}
        solution_3 = module_0.Solution(**dict_0)
    except BaseException:
        pass
