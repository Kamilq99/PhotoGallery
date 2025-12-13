from datetime import datetime

class metadata:
    def __init__(self, tittle: str, description: str):
        self.tittle = tittle
        self.description = description
        self.send_at = datetime.utcnow()