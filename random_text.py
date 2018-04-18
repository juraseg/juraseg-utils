"""
Contains a funciton to generate random text
"""
from random import choice

_CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.!?:-; \n'


def random_text(length=100, chars=_CHARS):
    """
    Get a random string of length `length` containing of chars `chars`
    """
    return ''.join([choice(chars) for _ in xrange(0, length)])
