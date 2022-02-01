"""
    This module serves to validate integer data types,
    minimum and maximum values indicators
"""


class ValidType:
    def __init__(self, type_, min_value=None, max_value=None):
        """
        param set to None by default
        type_(data type): any data type: int, float, str
        min_value(int): the minimum value allowed
        max_value: maximum value allowed
        return: self if instance is None else instance value
        """
        self._type = type_
        if min_value is not None and max_value is not None:
            if not isinstance(min_value, int) or not isinstance(max_value,int):
                raise ValueError(f"Must be an integer value ")
            if min_value < 0 or max_value < 0:
                raise ValueError(f"Must be a positive integer value ")
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, cls, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, self._type):
            raise ValueError(f"{value} must be {self._type.__name__}")
            
        if self.min_value is not None and self.max_value is not None:
            if isinstance(value, int):
                if value < self.min_value:
                    raise ValueError(f"{self.name} must be at least {self.min_value}")
                if value > self.max_value:
                    raise ValueError(f"{self.name} must not exceed {self.max_value}")
            else:
                if len(value) < self.min_value:
                    raise ValueError(f"{self.name} must be at least {self.min_value}")
                if len(value) > self.max_value:
                    raise ValueError(f"{self.name} must not exceed {self.max_value}")

        instance.__dict__[self.name] = value

    def __get__(self, instance, cls):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, None)
