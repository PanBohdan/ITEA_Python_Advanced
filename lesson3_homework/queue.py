class Queue:
    def __init__(self, values=[]):
        self._values = values

    def enqueue(self, value):
        self._values.insert(0, value)

    def dequeue(self):
        if not len(queue._values) == 0:
            return self._values.pop(0)
        else:
            raise Exception('queue underflow (there is no objects in queue)')

    def first(self):
        if not len(queue._values) == 0:
            return self._values[0]
        else:
            raise Exception('queue underflow (there is no objects in queue)')

    def swap(self):
        length = len(self._values)
        if not length < 2:
            self._values[0], self._values[1] = self._values[1], self._values[0]

    def last(self):
        if not len(self._values) == 0:
            return self._values[len(self._values)-1]
        else:
            raise Exception('queue underflow (there is no objects in queue)')

    def clear(self):
        self._values.clear()

    def is_empty(self):
        if len(self._values) == 0:
            return True
        else:
            return False


# tests
queue = Queue([5, 4, 3, 2, 1])
queue.enqueue(6)
print(queue.dequeue())
print(queue.first())
queue.swap()
print(queue.first())
print(queue.last())
