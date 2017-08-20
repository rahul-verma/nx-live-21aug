import types
import numbers

class Value(object):

    def __init__(self, name, value, **kwargs):
        self._name = name
        self._value = value
        self.populate(**kwargs)
        self.validate()

    def get_name(self):
        return self._name

    def get_value(self):
        return self._value

    def populate(self, **kwargs):
        pass

    def is_valid(self):
        pass

    def validate(self):
        if not self.is_valid():
            raise Exception("Invalid value >>{1}<< supplied for '{0}'. Expected: {2}".format(self._name, self._value, self.__class__.__name__))

class NonEmptyString(Value):

    def is_valid(self):
        return type(self.get_value()) is types.StringType and len(self.get_value()) > 0

class PositiveNumber(Value):

    def is_valid(self):
        return isinstance(self.get_value(), numbers.Number) and self.get_value() >= 0

class Integer(Value):

    def is_valid(self):
        return isinstance(self.get_value(), int)

class PositiveInteger(Integer):

    def is_valid(self):
        return super(PositiveInteger, self).is_valid() and self.get_value() >= 0

class RangeBoundInteger(Integer):

    def __init__(self, name, value, start, end):
        super(RangeBoundInteger, self).__init__(name, value, start=start, end=end)

    def populate(self, start, end):
        self._start = start
        self._end = end

    def is_valid(self):
        name = self.get_name()
        value = self.get_value()
        return super(RangeBoundInteger, self).is_valid() and value >= self._start and value <= self._end

if __name__ == "__main__":
    # Should work
    a = NonEmptyString('a', "abc")
    a = Integer('a', 1)
    a = Integer('a', -1)
    a = PositiveNumber('a', 1)
    a = PositiveNumber('a', 1.2)
    a = PositiveInteger('a', 1)
    a = RangeBoundInteger('a', 1, 0, 2)

    # Should not
    #a = NonEmptyString('a', 1)
    #a = NonEmptyString('a', "")
    #a = Integer('a', "a")
    #a = Integer('a', 1.2)
    #a = PositiveNumber('a', "abc")
    #a = PositiveNumber('a', -1)
    #a = PositiveNumber('a', -1.2)
    #a = PositiveInteger('a', -1)
    #a = PositiveInteger('a', 1.2)
    #a = PositiveInteger('a', -1.2)
    #a = RangeBoundInteger('a', -1, 0, 2)
    #a = RangeBoundInteger('a', 1.2, 0, 2)