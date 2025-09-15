class Matrix:
    def __init__(self, columns, rows):
        if columns <= 0 or rows <= 0:
            raise ValueError("Number of columns and rows must be positive integers.")
        self.columns = columns
        self.rows = rows
        self.data = [[0 for _ in range(columns)] for _ in range(rows)]

    def __getitem__(self, pos):
        if not isinstance(pos, tuple) or len(pos) != 2:
            raise TypeError("Index must be a tuple (column, row).")
        c, r = pos
        if not (0 <= r < self.rows) or not (0 <= c < self.columns):
            raise IndexError("Matrix index out of range.")
        return self.data[r][c]

    def __setitem__(self, pos, value):
        if not isinstance(pos, tuple) or len(pos) != 2:
            raise TypeError("Index must be a tuple (column, row).")
        c, r = pos
        if not (0 <= r < self.rows) or not (0 <= c < self.columns):
            raise IndexError("Matrix index out of range.")
        self.data[r][c] = value

    def __str__(self):
        return "\n".join(str(row) for row in self.data)


# דוגמה
m = Matrix(3, 2)
m[1, 0] = 5
print(m[1, 0])
print(m)
