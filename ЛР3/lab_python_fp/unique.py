class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen=set()
        self.iterator=iter(items)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            item=next(self.iterator)
            key=item.lower() if self.ignore_case and isinstance(item,str) else item
            if key not in self.seen:
                self.seen.add(key)
                return item

if __name__=='__main__':
    data=['a','A','b','B','a']
    print(list(Unique(data)))
    print(list(Unique(data,ignore_case=True)))
