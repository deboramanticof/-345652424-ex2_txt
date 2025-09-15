class SkipIterator:
    def __init__(self, data, k):
        self.data = data
        self.k = k
        self.index = k - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += self.k
        return value


# דוגמה
natural_numbers = [i for i in range(1, 50)]
skip_iterator = SkipIterator(natural_numbers, 5)

for num in skip_iterator:
    print(num, end=",")
print()
