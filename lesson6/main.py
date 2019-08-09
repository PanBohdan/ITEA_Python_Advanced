class CustomList(object):
    def __init__(self, elements):
        if isinstance(elements, list):
            self._my_custom_list = elements
        else:
            raise TypeError('Put list in a list')

    def __setitem__(self, index, value):
        self._my_custom_list[index] = value

    def __getitem__(self, index):
        return self._my_custom_list[index]

    def __str__(self):
        return str(self._my_custom_list)

    def __add__(self, other):
        if isinstance(other, CustomList):
            return CustomList(self._my_custom_list+other.get_list())
        else:
            raise TypeError('Can add list only to a list')

    def get_list(self):
        return self._my_custom_list

    def pop(self, index):
        tmp = self._my_custom_list[index]
        del self._my_custom_list[index]
        return tmp

    def append(self, item):
        self._my_custom_list = self._my_custom_list + [item]

    def insert(self, index, item):
        s_l = self._my_custom_list  # short_list
        self._my_custom_list = s_l[0: index] + [item] + s_l[index: len(s_l)]

    def remove(self, what_to_remove):
        for j in range(len(self._my_custom_list)-1):
            if self._my_custom_list[j] == what_to_remove:
                del self._my_custom_list[j]

    def clear(self):
        self._my_custom_list = []


class CustomDict:
    def __init__(self, elements):
        if isinstance(elements, dict):
            self._my_custom_dict = elements
        else:
            raise TypeError('Put dict in a dict')

    def __getitem__(self, index):
        return self._my_custom_dict[index]

    def __str__(self):
        return str(self._my_custom_dict)

    def __add__(self, other):
        if isinstance(other, CustomDict):
            tmp = self._my_custom_dict
            tmp.update(other.get_dict())
            return CustomDict(tmp)
        else:
            raise TypeError('Can add dict only to a dict')

    def get_dict(self):
        return self._my_custom_dict

    def get(self, item):
        return self._my_custom_dict[item]

    def items(self):
        return self._my_custom_dict

    def keys(self):
        keys_list = []
        for j in self._my_custom_dict:
            keys_list.append(j)
        return keys_list

    def values(self):
        keys_list = []
        for j in self._my_custom_dict:
            keys_list.append(j)
        values_list = []
        for k in keys_list:
            values_list.append(self._my_custom_dict[k])
        return values_list


# all testing here
x = CustomList([1, 2, 3, 4])
for i in x:
    print(i)
y = CustomList([6])
x[0] = '5'
print(x.pop(0))
print(x)
print(x[2])
x.append(5)
print(x)
x.insert(0, 1)
print(x)
x.remove(2)
print(x)
z = x + y
print(z)

d = CustomDict({1: 2, 3: 4})
print(d.get(1))
print(d[1])
print(d.items())
print(d.keys())
print(d.values())
d1 = CustomDict({5: 6})
fin_d = d+d1
print(fin_d)
print(z+1)  # TypeError
