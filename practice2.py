x = {'x': 3, 'y': 4, 'z': 5}
y = {"x": 3, "y": 1, "z": 1}

shared_items = {k: x[k] for k in x if k in y and x[k] == y[k]}
print(shared_items)
