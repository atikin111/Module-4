class MyDict:
    def __init__(self):
        self.my_dict = {}

    def __getitem__(self, key):
        return self.my_dict.get(key, None)

    def __contains__(self, key):
        return key in self.my_dict

    def __setitem__(self, key, value):
        self.my_dict[key] = value

    def __delitem__(self, key):
        if key not in self.my_dict:
            pass
        else:
            del self.my_dict[key]

    def keys(self):
        return list(self.my_dict.keys())

    def values(self):
        return list(self.my_dict.values())

    def items(self):
        return list(self.my_dict.items())

    def __str__(self):
        return str(self.my_dict)


if __name__ == "__main__":
    my_dict = MyDict()
    my_dict['name'] = 'Alice'
    my_dict['age'] = 30
    print(my_dict['name'])  # Вернет 'Alice'
    print('city' in my_dict)  # Вернет False
    del my_dict['age']
    print(my_dict.keys())  # Вернет ['name']
    print(my_dict.values())  # Вернет ['Alice']