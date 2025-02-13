import unittest
from workflows.main_workflow import coa_workflow

def run_workflow():
    print("Running CoA Workflow...")
    sample_data = {"sales": 5000, "region": "North America"}
    result = coa_workflow(sample_data)
    print("Workflow Result:", result)

def run_tests():
    print("Running Unit Tests...")
    loader = unittest.TestLoader()
    suite = loader.discover("tests", pattern="test_*.py")
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_workflow()
    run_tests()