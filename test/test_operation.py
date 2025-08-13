from src.mathoperation import add, sub
def test_add():  # Added colon
    assert 1 + 1 == 2
    assert add(-1, 1) ==0

def test_sub():
    assert sub(5, 3) == 2
    assert sub(4, 3) == 1
    assert sub(3, 3) == 0
    assert sub(2, 3) == -1