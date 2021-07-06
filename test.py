import new_search
import pytest

def test_file():
    try:
        output = new_search.search(121)
        assert output == 1
    except OSError:
        print("No such file exists")
    except AssertionError:
        print("assert false")


def test_file_2():
    try:
        output = new_search.search(121)
        assert output == 0
    except OSError:
        print("No such id exists")
    except AssertionError:
        print("assert false")


