fs = frozenset([1, 2, 3])
print("לפני:", fs)

try:
    fs.add(4)
except AttributeError as e:
    print("שגיאה:", e)

#נוצרת שגיאה:
#'frozenset' object has no attribute 'add'
#כלומר לא ניתן לשנות את האובייקט
#frozenset הוא immutable
