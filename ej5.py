class CountedObject:
    total_created = 0
    currently_alive = 0

    def __init__(self):
        CountedObject.total_created += 1
        CountedObject.currently_alive += 1
        self.number_serial = CountedObject.total_created

    def __del__(self):
        CountedObject.currently_alive -= 1

    @staticmethod
    def allocated_num():
        return CountedObject.currently_alive


# דוגמה
obj1 = CountedObject()
obj2 = CountedObject()
obj3 = CountedObject()

print(CountedObject.allocated_num())  # 3

del obj2
print(CountedObject.allocated_num())  # 2

del obj1
del obj3
print(CountedObject.allocated_num())  # 0
