from nose.tools import *
from ex49.parser import *


def test_peek():
    test = [('noun', 'bear'),('verb', 'go'),('stop', 'it')]
    assert_equal(peek(test), 'noun')
    test = test[1:]
    assert_equal(peek(test), 'verb')
    assert_equal(peek(None), None)
    
def test_match():
    test = [('noun', 'bear'),('verb', 'go'),('stop', 'it')]
    assert_equal(match(test, 'noun'), ('noun', 'bear'))
    assert_equal(match(test, 'stop'), None)
    assert_equal(match(None, 'stop'), None)
  
def test_parse_verb():
    test = [('noun', 'bear'), ('verb', 'go'),('stop', 'to')]
    assert_equal(parse_verb(test), ('verb', 'go'))