import pytest
from six import StringIO
from main import find_words_with_letters


TESTING_WORDS = """
xjas
RMOTR
ogah3
vermont
32aa
uppermost
g8ad8d
temporize
z8aji
"""


def test_find_many_words():
    words_file = StringIO(TESTING_WORDS)
    words_iter = (word.strip().lower() for word in words_file if word.strip())
    words = iter(find_words_with_letters(words_iter, 'rmot'))
    assert next(words) == 'RMOTR'
    assert next(words) == 'vermont'
    assert next(words) == 'uppermost'
    with pytest.raises(StopIteration):
        next(words)


def test_find_only_one_word():
    words_file = StringIO(TESTING_WORDS)
    words_iter = (word.strip().lower() for word in words_file if word.strip())
    words = iter(find_words_with_letters(words_iter, '2a'))
    assert next(words) == '32aa'
    with pytest.raises(StopIteration):
        next(words)


def test_wrong_order():
    words_file = StringIO(TESTING_WORDS)
    words_iter = (word.strip().lower() for word in words_file if word.strip())
    words = iter(find_words_with_letters(words_iter, '8z'))
    with pytest.raises(StopIteration):
        next(words)
