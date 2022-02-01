"""
    Test the integer validator class
    command line: python -m pytest test/unit/test_integer_validator.py
"""

from descriptor.utils.validator import ValidType
import pytest


@pytest.fixture
def validator_values():
    return {
        "_type": int,
        "min_value": 1,
        "max_value": 100
    }


@pytest.fixture
def validator(validator_values):
    return ValidType(**validator_values)


def test_initiate_validator(validator, validator_values):
    for attr_name in validator_values:
        assert getattr(validator, attr_name) == validator_values.get(attr_name)


@pytest.mark.parametrize(
    "min_value, exception", [(1.2, ValueError), (-1.2, ValueError)]
)
def test_valid_min_value_error(min_value, exception, validator_values):
    validator_values["min_value"] = min_value
    with pytest.raises(exception):
        ValidType(**validator_values)


@pytest.mark.parametrize(
    "max_value, exception", [(1.2, ValueError), (-1.2, ValueError)]
)
def test_valid_max_value_error(max_value, exception, validator_values):
    validator_values["max_value"] = max_value
    with pytest.raises(exception):
        ValidType(**validator_values)
