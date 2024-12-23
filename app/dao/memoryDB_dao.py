
class MemoryDB:
    def __init__(self) -> None:
        self.hashmap = {}

    def get(self, key):
        if key not in self.hashmap:
            raise ValueError("Error")

    def set(self, key, value):
        pass

    def delete(self, key):
        pass

    def keys(self):
        pass
