import unittest
import json
from student_age import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.credentials = ('toto', 'python')


    def test_get_student_ages_unauthorized(self):
        response = self.app.get('/pozos/api/v1.0/get_student_ages')
        self.assertEqual(response.status_code, 401)

    def test_get_student_ages_authorized(self):
        response = self.app.get('/pozos/api/v1.0/get_student_ages', 
                                headers={'Authorization
                                


if __name__ == '__main__':
    unittest.main()
