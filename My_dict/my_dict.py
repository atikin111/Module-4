from typing import Any

class MyDict:
    def __init__(self):
        self.size = 8
        self.table = [None] * self.size


    def _get_hash(self, key) -> int: # Возвращает индекс в хэш-таблице для ключа
        return hash(key) % self.size


    def _resize(self) -> None:

           '''Увеличивает размер хэш-таблицы в два раза и переносит все элементы в новую.'''

           old_table = self.table
           self.size *= 2
           self.table = [None] * self.size

           for item in old_table:
               if item is not None:
                   _, key, value = item
                   self.add(key, value)


    def __setitem__(self, key, value) -> None:

        '''Добавляет пару key-value в хэш-таблицу'''

        key_hash = self._get_hash(key) # Получаем хэш ключа

        if self.table[key_hash] is None: #  Если ячейка пуста, то добавляем hash и key-value
            self.table[key_hash] = (key_hash, key, value)
        else:
            # Иначе ищем свободную ячейку для добавления пары key-value
            new_hash = self._probe(key_hash)

            # Если нашли свободную ячейку, то добавляем пару key-value
            if new_hash:
                self.table[new_hash] = (key_hash, key, value)
            else:
                # Иначе увеличиваем размер таблицы и повторно добавляем пару ключ-значение
                self._resize()
                self.add(key, value)


    def _probe(self, start_index) -> int | None:

        '''Ищем свободную ячейку для добавления пары key-value'''

        # Проходим по всем ячейкам в хэш-таблице
        for i in range(start_index + 1, self.size + start_index):
            index = i % self.size
            if self.table[index] is None:
                return index


    def __getitem__(self, key) -> Any | None:

        '''Возвращает значение по ключу'''

        # Получаем хэш ключа
        key_hash = self._get_hash(key)

        # Если ячейка не пуста и ключ совпадает, то возвращаем значение
        if self.table[key_hash] is not None and self.table[key_hash][1] == key:
            return self.table[key_hash][2]
        else:
            # Иначе ищем значение по ключу
            for i in range(key_hash + 1, self.size + key_hash):
                index = i % self.size
                if self.table[index] is not None and self.table[index][1] == key:
                    return self.table[index][2]


    def __delitem__(self, key) -> bool:

        '''Удаляет значение по ключу'''

        key_hash = self._get_hash(key)
        if self.table[key_hash] is not None and self.table[key_hash][1] == key:
            self.table[key_hash] = None
            return True
        else:
            for i in range(key_hash + 2, self.size + key_hash):
                index = i % self.size
                if self.table[index] is not None and self.table[index][1] == key:
                    self.table[index] = None
                    return True
        return False


    def keys(self):
        return [key[1] for key in self.table if key is not None]


    def values(self):
        return [value[2] for value in self.table if value is not None]


    def items(self):
        return [item for item in self.table if item is not None]


    def __str__(self):
        result = ''
        for item in self.table:
            if item is not None:
                result += str(item) + '\n'
        return result


my_dict = MyDict()
my_dict['name'] = 'Alice'
# my_dict['1'] = '1'
# my_dict['2'] = '2'
# my_dict['3'] = '3'
# my_dict['4'] = '4'
# my_dict['5'] = '5'
# my_dict['6'] = '6'
# my_dict['7'] = '7'
my_dict['age'] = 30
print(my_dict['name'])  # Вернет 'Alice'
print('city' in my_dict.keys())  # Вернет False
del my_dict['age']
print(my_dict.keys())  # Вернет ['name']
print(my_dict.values())  # Вернет ['Alice']