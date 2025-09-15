class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def first(self):
        return self._first

    @first.setter
    def first(self, value):
        if len(value) < 2:
            raise ValueError("First name must have at least 2 characters")
        self._first = value

    @property
    def last(self):
        return self._last

    @last.setter
    def last(self, value):
        if len(value) < 2:
            raise ValueError("Last name must have at least 2 characters")
        self._last = value


# דוגמה
p = Person("Debora", "Manticof")
print(p.first, p.last)

try:
    p.first = "A"
except ValueError as e:
    print(e)
