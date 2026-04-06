class MyHashSet:

    def __init__(self):
        self.arr = [] 

    def add(self, key: int) -> None:
        if not key in self.arr:
            self.arr.append(key)

    def remove(self, key: int) -> None:
        if key in self.arr:
            self.arr.remove(key)

    def contains(self, key: int) -> bool:
        return True if key in self.arr else False