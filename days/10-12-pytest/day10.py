import pytest


def run():
    pass


def test_always_pass():
    assert True


def test_always_fails():
    assert 1 == 2


def _exception():
    raise SystemExit(1)


def test_exception():
    with pytest.raises(SystemExit):
        _exception()


class TestClass:
    def test_one(self):
        x = 'this'
        assert 'h' in x

    def test_two(self):
        x = 'hello'
        assert hasattr(x, 'check')
