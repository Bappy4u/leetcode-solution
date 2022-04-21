class MyHashSet:

    def __init__(self):
        self.list = set()

    def add(self, key: int) -> None:
        if key not in self.list:
            self.list.add(key)
        

    def remove(self, key: int) -> None:
        if key in self.list:
            self.list.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.list
