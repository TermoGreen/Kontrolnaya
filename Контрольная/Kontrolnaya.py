class _3:
    def __init__(self, List):
        self.List = List
    def add_theme(self, value):
        self.value = value
        self.List.append(value)
        return self.List
    def shift_one(self):
        self.List = self.List[-1:] + self.List[:-1]
    def reverse_order(self):
        self.List = list(reversed(self.List))
    def get_themes(self):
        return self.List
    def get_first(self):
        return self.List[0]
    def List_info(self):
        print(self.List)

lst = ["Крокодилы", "Помидоры", "Огурцы", "Пингвины"]
ex = _3(lst)
ex.add_theme("Рыбки")
ex.List_info()
ex.shift_one()
ex.List_info()
ex.reverse_order()
ex.List_info()
ex.get_first()
ex.List_info()
ex.get_themes()
ex.List_info()
