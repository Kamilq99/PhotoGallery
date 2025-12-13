from model.wallpaper import wallpaper
from model.metadata import metadata

class image:
    def __init__(self, wallpaper: wallpaper, metadata: metadata):
        self.wallpaper = wallpaper
        self.metadata = metadata