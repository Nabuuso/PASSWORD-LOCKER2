import unittest # Importing the unittest module
from user import user # Importing the user class

class Testuser(unittest.TestCase):
    
    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    
    # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = user("user_name","password") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.user_name.user_name)
        self.assertEqual(self.password.password)
       
        


if __name__ == '__main__':
    unittest.main()