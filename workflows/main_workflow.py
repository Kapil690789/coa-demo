from agents.validator import Validator
from agents.analyzer import Analyzer
from agents.notifier import Notifier
import threading

def coa_workflow(input_data):
    # Initialize agents
    validator = Validator()
    analyzer = Analyzer()
    notifier = Notifier()

    # Execute workflow
    validated = validator.run(input_data)
    if validated["status"] == "valid":
        analyzed = analyzer.run(validated["data"])
        notifier.run(analyzed)
        return {"result": "Workflow completed"}
    else:
        return {"error": validated["error"]}

if __name__ == "__main__":
    sample_data = {"sales": 5000, "region": "North America"}
    result = coa_workflow(sample_data)
    print(result)