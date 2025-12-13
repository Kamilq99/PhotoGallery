import uuid

class wallpaper:
    def __init__(self, filename: str, content_type: str):
        self.id = str(uuid.uuid4())
        self.filename = filename
        self.content_type = content_type

    @property
    def s3_key(self) -> str:
        return f"wallpapers/{self.id}/{self.filename}"