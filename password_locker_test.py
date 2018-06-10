import unittest # Importing the unittest module
from password_locker import User # Importing the User class

def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_User = User("David","Password","kd.kinuthiadavid@gmail.com") # create user object


def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''

    self.assertEqual(self.new_User.user_name,"David")
    self.assertEqual(self.new_User.password,"Password")
    self.assertEqual(self.new_User.email,"kd.kinuthiadavid@gmail.com")


if __name__ == '__main__':
    unittest.main()
