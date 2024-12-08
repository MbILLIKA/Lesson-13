from functions import hello_who, salary

def test_hello_who_max():
    assert hello_who('Max') == 'Hello, Max'
    assert hello_who('Max1') == 'Hello, Max1'
    assert hello_who('Max2') == 'Hello, Max2'
    assert hello_who('Max3') == 'Hello, Max3'

def test_salary():
    assert(2, 2) != 8
    assert(3, 1) != 6