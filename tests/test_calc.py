from src.calc import example_function_add

def test_example_function_add():
    assert example_function_add(0, 0) == 0
    assert example_function_add(0, 1) == 1
    assert example_function_add(1, 1) == 2
