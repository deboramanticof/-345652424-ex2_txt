s = {1, 2, 3}
lst = [4, 5]

s.add(lst)

#TypeError: unhashable type: 'list'
#Lists are mutable, so they are not hashable
#Sets can only contain immutable (hashable) items like numbers, strings, or tuples
