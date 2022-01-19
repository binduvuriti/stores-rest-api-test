from models.user import UserModel
from tests.unit.base_test import UnitBaseTest

class UserTest(UnitBaseTest):
    def test_create_user(self):
        user = UserModel('name', 'pwd')
        self.assertEqual('name', user.username)
        self.assertEqual('pwd', user.password)




