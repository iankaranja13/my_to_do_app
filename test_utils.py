import unittest
from task import Task
from utils import generate_id

class TestUtils(unittest.TestCase):

    def test_generate_id_empty(self):
        tasks = []
        self.assertEqual(generate_id(tasks), 1)

    def test_generate_id_existing(self):
        tasks = [Task(1, "Test", "desc"), Task(2, "Another", "desc")]
        self.assertEqual(generate_id(tasks), 3)

if __name__ == '__main__':
    unittest.main()
