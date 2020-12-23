# module for playing with pytest package
import pytest
import calc

# test fixtures
#def setup_module(module):
#    print("setup")
#
#def teardown_module(module):
#    print("teardown")

# or
@pytest.fixture()
def writeMethod():
    print("start")
    yield
    print("stop")

#@pytest.mark.number # decorator usage
#@pytest.mark.skipif(1+1==3, reason="1+1 is not 3") # conditional execution
def test_add(writeMethod):
    assert calc.add(1,14) == 15
    assert calc.add(1,12) == 13


def test_multiply():
    assert calc.multiply(1, 12) == 12

def test_add2(writeMethod):
    assert calc.add(1,14) == 15
    assert calc.add(1,12) == 13

# paramterized TCs
@pytest.mark.parametrize('a, b, result',
                         [
                             (7, 3, 10),
                             (1, 3, 4),
                             ('a', 'b', 'ab')

                         ])
def test_add_parametrized(a, b, result):
    assert calc.add(a,b) == result

# cmd pytest --html=92_pytest_results\report.html test_module_pytest.py to generate html report
