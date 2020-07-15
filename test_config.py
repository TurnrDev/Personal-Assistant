import pytest

from papy import utils

def func(x):
    utils.config.set('username', x)
    return utils.config.get('username')


def test_answer():
    assert func('Jay') == 'Jay'
