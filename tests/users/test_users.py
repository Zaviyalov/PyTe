import pytest

from src.baseclasses.response import Response
from src.schemas.user import User


#
# res = requests.get(SERVICE_URL)
# # print(res.json())

def test_getting_users_list(get_user, get_number, make_number):
    Response(get_user).assert_status_code(200).validate(User)
    # print(make_number)

@pytest.mark.developmet
@pytest.mark.parametrize('first_value, second_value, result', [
    (1, 2, 3),
    (-1, -2, -3),
    (-1, 2, 1)
])
def test_calculate(first_value, second_value, result, calculate):
    assert calculate(first_value, second_value) == result
