class Stack:
    def __init__(self, values=[], stack_size=1):
        if not len(values) > stack_size:
            self._values = values
            self._stack_size = stack_size
        else:
            raise Exception('cannot insert more values than stack size')

    def push(self, what_to_push):
        if not len(self._values) == self._stack_size:
            self._values.insert(len(self._values), what_to_push)
        else:
            raise Exception('stack overflow '
                            '(there max number of objects in stack)')

    def pop(self):
        if not len(self._values) == 0:
            return self._values.pop(len(self._values)-1)
        else:
            raise Exception('stack underflow (there is no objects in stack)')

    def top(self):
        if not len(self._values) == 0:
            return self._values[len(self._values)-1]
        else:
            raise Exception('stack underflow (there is no objects in stack)')

    def swap(self):
        length = len(self._values)
        if not length < 2:
            self._values[length-1], self._values[length-2] = \
                self._values[length-2], self._values[length-1]
        else:
            pass

    def clear(self):
        self._values.clear()

    def is_empty(self):
        if len(self._values) == 0:
            return True
        else:
            return False

    def is_full(self):
        if len(self._values) == self._stack_size:
            return True
        else:
            return False

    def size(self):
        return len(self._values)


# tests
stack = Stack([1, 2, 3], 25)
stack.push(4)
print(stack.size())
print(stack.pop())
print(stack.pop())
print(stack.top())
stack.swap()
print(stack.top())
stack.swap()
print(stack.top())
print(stack.is_empty())
stack.clear()
print(stack.is_empty())
print(stack.is_full())
