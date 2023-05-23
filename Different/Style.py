class Style:
    def __init__(self, **args):
        self.data = {}
        self.data.update(args)
        self.unknown = []

    def __getattr__(self, item):
        if item in self.data:
            return self.data[item]

        if item not in self.unknown:
            self.unknown.append(item)
            print('Style: requested unknown type "%s"' % item)

        return 1
