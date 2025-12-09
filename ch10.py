# 1 -> Context Manager
import time
class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self , *args):
        self.end = time.time()
        print(f"execution took {self.end - self.start} seconds")

with Timer():
    for i in range(1000000):
        pass

# -----------------------------------------------
# 2 -> Generator
def even_numbers(n):
    for i in range(2, n, 2):
        yield i

for num in even_numbers(10):
    print(num)

# -----------------------------------------------
# 3 -> Coroutine
def filter_positive():
    while True:
        num = yield
        if num > 0:
            print(f"positive number: {num}")

co = filter_positive()
next(co)
co.send(-3)
co.send(5)
co.send(0)


# -----------------------------------------------
# 4 -> Factory Pattern
class Circle:
    def draw(self):
        return "drawing a circle"

class Square:
    def draw(self):
        return "a square is being drawn."

def shape_factory(shape_type):
    if shape_type == "circle":
        return Circle()
    elif shape_type == "square":
        return Square()
    else:
        raise ValueError("Unknown shape")

shape = shape_factory("circle")
print(shape.draw())

# -------------------------------------------------
# 5 -> Observer pattern

class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, obs):
        self.observers.append(obs)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

class Observer:
    def update(self, message):
        print(f"received update: {message}")

subject = Subject()
observer1 = Observer()
observer2 = Observer()
subject.attach(observer1)
subject.attach(observer2)
subject.notify("update available!")
