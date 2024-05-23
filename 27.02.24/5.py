def same_by(charecteristic, objects):
    if len(objects) == 0:
        return True
    first_value = charecteristic(objects[0])
    for obj in objects:
        if charecteristic(obj) != first_value:
            return False
    return True

values = [0, 2, 10, 6, 7]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')