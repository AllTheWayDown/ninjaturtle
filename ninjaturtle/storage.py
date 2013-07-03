STORAGE_SIZE = 4

class SimpleStorage(object):
    def get_storage(self):
        return [0 for i in range(STORAGE_SIZE)]

class ArrayStorage(object):
    def __init__(self, num_turtles=256):
        self.array = array('f'),
        self.num_turtles = size
        self.turtles = []
        self.extend(size)
        self.current = 0

    def extend(self, size):
        self.view.release()
        for view in self.views.values():
            view.release()
        self.array.extend([0] * size * STORAGE_SIZE)
        self.view = memoryview(self.array)




