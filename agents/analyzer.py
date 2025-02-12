class Analyzer:
    def __init__(self):
        self.task = "Analyze data"

    def run(self, data):
        if "sales" in data:
            data["insights"] = f"Sales increased by {data['sales'] * 0.1}%"
            return {"status": "analyzed", "data": data}
        else:
            return {"status": "error", "error": "No sales data found"}