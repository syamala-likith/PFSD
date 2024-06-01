import pytest

@pytest.mark.parametrize("num, output",[(1,11),(2,22),(4,44)])
def test_multiplication_11(num, output):
   assert 11*num == output