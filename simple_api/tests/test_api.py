import unittest
import json
from student_age import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        # Credentials for basic auth
        self.credentials = ('toto', 'python')

    def test_get_student_ages_unauthorized(self):
        """Test getting student ages without authentication"""
        response = self.app.get('/pozos/api/v1.0/get_student_ages')
        self.assertEqual(response.status_code, 401)

    def test_get_student_ages_authorized(self):
        """Test getting student ages with authentication"""
        response = self.app.get('/pozos/api/v1.0/get_student_ages', 
                              auth=self.credentials)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn('student_ages', data)

    def test_get_student_age_not_found(self):
        """Test getting age of non-existent student"""
        response = self.app.get('/pozos/api/v1.0/get_student_ages/nonexistent', 
                              auth=self.credentials)
        self.assertEqual(response.status_code, 404)

    def test_get_student_age_success(self):
        """Test getting age of existing student"""
        # First, get all students to find an existing one
        response = self.app.get('/pozos/api/v1.0/get_student_ages', 
                              auth=self.credentials)
        data = json.loads(response.data)
        if data['student_ages']:
            # Get first student from the list
            student_name = next(iter(data['student_ages']))
            response = self.app.get(f'/pozos/api/v1.0/get_student_ages/{student_name}', 
                                  auth=self.credentials)
            self.assertEqual(response.status_code, 200)
            # The response should be the age (an integer)
            age = json.loads(response.data)
            self.assertIsInstance(age, int)

if __name__ == '__main__':
    unittest.main()
