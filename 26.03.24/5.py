class DefaultList(list):
    def __init__(self, default_value):
        self.default_value = default_value
        super().__init__()

    def __getitem__(self, index):
        try:
            return super().__getitem__(index)
        except IndexError:
            return self.default_value

my_list = DefaultList(default_value=0)
print(my_list[0])  # Выведет: 0, так как список пустой и индекс 0 выходит за границы
my_list.append(1)
my_list.append(2)
print(my_list[0])  # Выведет: 1, так как элемент с индексом 0 существует
print(my_list[5])  # Выведет: 0, так как индекс 5 выходит за границы списка и будет возвращено значение по умолчанию