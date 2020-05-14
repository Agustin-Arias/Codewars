class DefaultList:
    def __init__(self, list, default):
        self.list = list
        self.default = default

    def __repr__(self):
        return f"{self.list}"

    def __getitem__(self, key):
        print(self.list)
        try:
            return self.list[key]
        except IndexError:
            return self.default

    def extend(self, list_to_add):
        self.list = self.list + list_to_add

    def append(self, item):
        self.list.append(item)

    def insert(self, index, item):
        length = len(self.list)
        if index == length:
            self.list.append(item)
        else:
            try:
                if index < 0:
                    index += length
                self.list = self.list[:index] + [item] + self.list[index:]
            except IndexError:
                return self.default

    def remove(self, elem):
        ls = self.list
        for index, item in enumerate(ls):
            if item == elem:
                del self.list[index]
                break

    def pop(self, index = -1):
        length = len(self.list)
        try:
            del self.list[index]
        except IndexError:
            return self.default
