class Sentence:
    def __init__(self, string):
        self.string = string
        self.lst = string.split(" ")
        self.length = len(self.lst)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.length:
            raise StopIteration
        self.current = self.count
        self.count += 1
        return self.lst[self.current]


my_sentence = Sentence("This is a test")
for i in my_sentence:
    print(i)
