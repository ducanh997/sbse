# Automatically generated by Pynguin.
import src.flood_fill as module_0


def test_case_0():
    solution_0 = module_0.Solution()


def test_case_1():
    int_0 = None
    list_0 = [int_0]
    list_1 = [list_0, list_0, list_0, list_0]
    int_1 = 0
    solution_0 = module_0.Solution()
    list_2 = solution_0.floodFill(list_1, int_1, int_1, int_1)
    assert solution_0 is not None
    assert list_2 == [[0], [0], [0], [0]]


def test_case_2():
    int_0 = None
    list_0 = [int_0, int_0, int_0]
    list_1 = [list_0, list_0, list_0, list_0]
    int_1 = 0
    solution_0 = module_0.Solution()
    list_2 = solution_0.floodFill(list_1, int_1, int_1, int_1)
    assert solution_0 is not None
    assert list_2 == [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]


def test_case_3():
    int_0 = None
    list_0 = [int_0, int_0, int_0]
    list_1 = [list_0, list_0, list_0, list_0]
    int_1 = 0
    solution_0 = module_0.Solution()
    list_2 = solution_0.floodFill(list_1, int_1, int_1, int_1)
    assert solution_0 is not None
    assert list_2 == [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    list_3 = solution_0.floodFill(list_1, int_1, int_1, int_1)
    assert list_3 == [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]