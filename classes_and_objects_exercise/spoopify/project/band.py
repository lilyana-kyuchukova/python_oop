from typing import List

from project.album import Album
from project.song import Song


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums: List[Album] = list()

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):
        try:
            album = next(filter(lambda a: a.name == album_name, self.albums))
        except StopIteration:
            return f"Album {album_name} is not found."

        if album.published:
            return "Album has been published. It cannot be removed."

        self.albums.remove(album)
        return f"Album {album.name} has been removed."

    def details(self):
        result = [f"Band {self.name}"]
        [result.append(b.details()) for b in self.albums]

        return "\n".join(result)
