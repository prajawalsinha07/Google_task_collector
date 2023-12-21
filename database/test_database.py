import unittest
from database.database import DatabaseClass

class TestDatabase(unittest.TestCase):

    def setUp(self) -> None:
        self.db = DatabaseClass()
        self.db.Connect_to_Database()
        return super().setUp()
    
    def test_get_record_id(self):
        self.assertEqual(self.db.Get_Record_ID("MTgxOTI3NTM0ODg4MDQ2NTYyMjA6MDow"),('MTgxOTI3NTM0ODg4MDQ2NTYyMjA6MDow', '"p33wQ0rACp-Zv7A5j9uMd2v6nAk/1"', 'Complete Project Proposal', 'needsAction', '2023-12-18T08:36:46', '2023-12-20T23:59:59', None))

    def test_get_record_status(self):
        self.assertEqual(self.db.Get_Records_Status("completed"),[('MTgxOTI3NTM0ODg4MDQ2NTYyMjA6MDox', '"p33wQ0rACp-Zv7A5j9uMd2v6nAk/2"', 'Buy groceries', 'completed', '2023-12-18T15:22:30', None, '2022-10-17T15:22:30')])

    def tearDown(self) -> None:
        self.db.Close_Connection()
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()
