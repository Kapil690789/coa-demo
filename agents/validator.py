class Validator:
    def __init__(self):
        self.task = "Validate input data"

    def run(self, data):
        if isinstance(data, dict):
            return {"status": "valid", "data": data}
        else:
            return {"status": "invalid", "error": "Data format incorrect"}