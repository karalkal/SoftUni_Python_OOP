class dictionary_iter:
    def __init__(self, dict_obj: dict):
        self.dict_obj = dict_obj
        self.count = 0
        self.size_of_dict = len(self.dict_obj)

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == self.size_of_dict:
            raise StopIteration
        for k, v in self.dict_obj.items():
            self.count += 1
            k_v_pair = k, v
            self.dict_obj.pop(k)
            return k_v_pair


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
