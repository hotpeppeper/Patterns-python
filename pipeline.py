from itertools import islice

class Pipeline(object):

    def __init__(self, steps) -> None:
        super().__init__()
        self.steps = steps
        self._validate_steps()

    def _validate_steps(self):
        _, trans = zip(**self.steps)
        for t in trans:
            if not hasattr(t, 'fit'):
                raise TypeError('All intermediate steps should be '
                                'transformers and implement fit '
                                "'%s' (type %s) doesn't" % (t, type(t)))

    def _iter(self):
        for idx, (name, trans) in enumerate(self.steps):
            yield idx, name, trans

    def fit(self, X):
        for idx, name, trans in self._iter():
            X = trans.fit(X)
        return X


class Foo1:

    def fit(self, X):
        for x in X:
            yield x ** 2


class Foo2:

    def fit(self, X):
        for x in X:
            yield x * 2


class Foo3:

    def fit(self, X):
        for x in X:
            yield x + 2


if __name__ == '__main__':
    pipeline = Pipeline([('foo1', Foo1()), ('foo2', Foo2()), ('foo3', Foo3())])
    print(list(pipeline.fit([1,2,3,4])))