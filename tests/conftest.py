import pytest
from random import randrange


@pytest.fixture
def get_number():
    return randrange(1, 1000, 5)


@pytest.fixture
def make_number():
    # print('I get number')
    numb = randrange(1, 100, 2)
    yield numb
    # print(f'Number is {numb}')


def _calculate(a, b):
    return a + b


@pytest.fixture
def calculate():
    return _calculate
