"""
    Test the integer validator class
    command line: python -m pytest test/unit/test_person_class.py
"""

from descriptor.models.person import Person
import pytest


@pytest.fixture
def person_values():
    return {
        "first_name": "Zara",
        "last_name": "Bitenyo",
        "age": 18,
        "skills": ["Handsome", "Python", "Driving"]
        }


@pytest.fixture
def person_class(person_values):
    return Person(**person_values)


def test_create_person(person_class, person_values):
    for feature in person_values:
        getattr(person_class, feature) == person_values.get(feature)


@pytest.mark.parametrize(
    "first_name, exception", [(2, ValueError), ("f", ValueError),
                              ("Antananarivo", ValueError)]
                        )
def test_invalid_first_name(first_name, exception, person_values):
    person_values["first_name"] = first_name
    with pytest.raises(exception):
        Person(**person_values)


@pytest.mark.parametrize(
    "last_name, exception", [(2, ValueError), ("f", ValueError), ("Antananarivo", ValueError)]
                        )
def test_invalid_last_name(last_name, exception, person_values):
    person_values["first_name"] = last_name
    with pytest.raises(exception):
        Person(**person_values)


@pytest.mark.parametrize(
    "age, exception", [(-1, ValueError), (0, ValueError), ("a string", ValueError),
                       (300, ValueError)]
                        )
def test_invalid_age(age, exception, person_values):
    person_values["age"] = age
    with pytest.raises(exception):
        Person(**person_values)


@pytest.mark.parametrize(
    "skills, exception", [("some str", ValueError), (0, ValueError),
                          ([], ValueError), (["sk1", "sk2", "sk3", "sk4", "sk5"], ValueError)]
                        )
def test_invalid_age(skills, exception, person_values):
    person_values["skills"] = skills
    with pytest.raises(exception):
        Person(**person_values)


def test_eq_class(person_values):
    p1 = Person(**person_values)
    p2 = Person(**person_values)
    assert p1 == p2
    person_values["age"] = 12
    p2 = Person(**person_values)
    assert p1 != p2


def test_invalid_eq(person_values):
    p1 = Person(**person_values)
    p2 = "some obj"
    with pytest.raises(ValueError):
        assert p1 == p2


def test_repr_person(person_class):
    assert person_class.first_name in repr(person_class)
    assert person_class.last_name in repr(person_class)
    assert str(person_class.age) in repr(person_class.age)
    assert str(person_class.skills) in repr(person_class.skills)


def test_str_person(person_class):
    assert person_class.first_name in str(person_class)
    assert person_class.last_name in str(person_class)
    assert str(person_class.age) in str(person_class.age)
    assert str(person_class.skills) in str(person_class.skills)
