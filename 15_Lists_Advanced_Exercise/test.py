values = [1, 4, 5, 2, 10]

some_value = 3

values = [value + some_value if value <= some_value else value - some_value for value in values]
