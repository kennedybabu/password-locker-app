import unittest
from credentials import Credentials

class TestUser(unittest.TestCase):
    '''
    Test case that defines test cases for the usesr class behaviour
    '''

    def setUp(self):
        '''
        set up the method that will run before each test case
        '''

        self.new_credentials = Credentials("twitter", "cosmic254", "12345")

    def test_init(self):
        '''
        test that the credential object is initialised as expected
        '''

        self.assertEqual(self.new_credentials.platform_name, "twitter")
        self.assertEqual(self.new_credentials.platform_user_name, "cosmic254")
        self.assertEqual(self.new_credentials.platform_user_password, "12345")


    def test_save_credentials(self):
        '''
        Test whether the credential object is saved in the credential list
        '''

        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credential_requirements), 1)

    def tearDown(self):
        '''
        Tear down method that cleans up after each test case has run
        '''

        Credentials.credential_requirements = []

    def test_Save_multiple_credentials(self):
        '''
        Test to check whether we can save multiple credentials to the array
        '''

        self.new_credentials.save_credentials()
        test_credential = Credentials("instagram", "Brady", "09876")
        test_credential.save_credentials()
        self.assertEqual(len(Credentials.credential_requirements), 2)

    def test_display_all_credentials(self):
        '''
        Test whether all credentials are displayed back to the user
        '''

        self.assertEqual(Credentials.display_credentials(), Credentials.credential_requirements)


if __name__ == "__main__":
    unittest.main()
