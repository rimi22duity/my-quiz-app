from src.user import User
import unittest

class TestUser:
    def test_user_creation(self):
        user = User('Alice')
        self.assertEqual(user.name, 'Alice')

if __name__ == '__main__':
    unittest.main()