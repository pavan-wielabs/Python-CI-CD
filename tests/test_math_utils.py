from mymodule.math_utils import add, subtract

def test_add():
    assert add(2, 3) == 5
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 10) == 0

def test_divide():
    assert divide(6, 2) == 3
    assert divide(10, 5) == 2
    assert divide(-6, 3) == -2

    # Test division by zero
    with pytest.raises(ValueError):
        divide(10, 0)