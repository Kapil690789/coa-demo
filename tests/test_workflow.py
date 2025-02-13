import unittest
import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from workflows.main_workflow import coa_workflow

class TestWorkflow(unittest.TestCase):
    def test_valid_data(self):
        input_data = {"sales": 5000, "region": "North America"}
        result = coa_workflow(input_data)
        self.assertEqual(result["result"], "Workflow completed")

    def test_invalid_data(self):
        input_data = "invalid data"
        result = coa_workflow(input_data)
        self.assertIn("error", result)

if __name__ == "__main__":
    unittest.main()