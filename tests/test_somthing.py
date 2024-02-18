
from src.baseclasses.response import Response
from src.schemas.user import User


#
# res = requests.get(SERVICE_URL)
# # print(res.json())

def test_getting_users_list(get_user):
    Response(get_user).assert_status_code(200).validate(User)


