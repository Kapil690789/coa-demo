class Notifier:
    def __init__(self):
        self.task = "Notify stakeholders"

    def run(self, data):
        if "insights" in data:
            print(f"Notification: {data['insights']}")
            return {"status": "notified", "data": data}
        else:
            return {"status": "error", "error": "No insights to notify"}