import unittest
import json
from src.app import app, get_db_connection

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        """ Set up test client before each test. """
        self.app = app.test_client()
        self.app.testing = True

    def test_get_tasks(self):
        """ Test the GET /api/tasks endpoint. """
        response = self.app.get('/api/tasks')
        self.assertEqual(response.status_code, 200)
        # Additional assertions can be added based on the expected response

    def test_create_task(self):
        """ Test the POST /api/tasks endpoint. """
        new_task = {
            'taskSource': 'Test',
            'taskDescription': 'Test task',
            'taskState': 'Pending',
            'timeAcquired': '2023-01-01T10:00:00Z',
            'timeCompleted': None
        }
        response = self.app.post('/api/tasks', data=json.dumps(new_task), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        # Additional assertions can be added based on the expected response

    # Optional: Additional tests for error cases or other endpoints

if __name__ == '__main__':
    unittest.main()
