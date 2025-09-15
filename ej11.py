def table_operation(list1, list2, operator):
    return [[operator(a, b) for b in list2] for a in list1]

def print_table(table):
    if not table:
        print("Table is empty.")
        return

    col_widths = [max(len(str(row[i])) for row in table) for i in range(len(table[0]))]

    for row in table:
        print("  ".join(str(val).rjust(col_widths[i]) for i, val in enumerate(row)))


# דוגמה 
if __name__ == "__main__":
    import operator
    list1 = [1, 2, 3]
    list2 = [10, 20, 30]
    add_table = table_operation(list1, list2, operator.add)
    print_table(add_table)
