class cfib:
    def __init__(self,maxnum):
        self.maxnum = maxnum
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a,self.b = self.b,self.a + self.b
        if self.a > self.maxnum:
            raise StopIteration()
        return self.a

    def __getitem__(self, item):
        if isinstance(item,int):
            for _ in range(item):
                self.__next__()
            return self.__next__()
        elif isinstance(item,slice):
            L = []
            start = item.start
            stop = item.stop
            if not start:
                start = 0
            for x in range(stop):
                if x >= start:
                    L.append(self.__next__())
                self.__next__()
            return L




fib = cfib(1000000)

print(fib[6])

print(fib[8:10])

for i in fib:
    print(i)

