import sys

class Person:
    def __init__(self, first, last):
        if len(first) < 2 or len(last) < 2:
            raise ValueError("Names must have at least 2 characters.")
        self.first = first
        self.last = last

    def __repr__(self):
        return f"{self.first} {self.last}"

def load_persons(filename):
    persons = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.split()
            if len(parts) >= 2:
                first, last = parts[0], parts[1]
                persons.append(Person(first, last))
    return persons

def sort_persons(persons, by="first"):
    if by == "first":
        return sorted(persons, key=lambda p: p.first)
    elif by == "last":
        return sorted(persons, key=lambda p: p.last)
    else:
        raise ValueError("Sort by 'first' or 'last' only.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ej8.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    persons = load_persons(filename)

    print(f"Loaded {len(persons)} persons from file.")
    print("First names:", [p.first for p in persons])
    print("Last names:", [p.last for p in persons])
    print()

    print("Sorted by first name:")
    for p in sort_persons(persons, by="first"):
        print(p)

    print("\nSorted by last name:")
    for p in sort_persons(persons, by="last"):
        print(p)
