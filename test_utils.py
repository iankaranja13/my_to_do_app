import unittest
import os
import json
import utils
from utils import load_file, save_file, task_id_generator, format_date, notify_user_overdue, delete_task, update_task_status

class TestUtils(unittest.TestCase):
    def test_load_file(self):
        """Test loading a file that exists."""

        test_data = [
            {"task_id": 1, "task_title": "Test Task", "task_description": "This is a test task."}
        ]
        test_file = "test_tasks.json"
        
        # Write test_data to a JSON file so load_file can read it
        with open(test_file, 'w') as f:
            import json
            json.dump(test_data, f)
        
        # Now test loading
        loaded_data = load_file(test_file)
        
        # Check loaded data matches what was saved
        self.assertEqual(loaded_data, test_data)
        
        # Clean up the test file after assertion
        import os
        os.remove(test_file)

    
if __name__ == "__main__":
    unittest.main()
