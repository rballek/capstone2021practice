"""
Tests for server
"""

from c21server.server import do_nothing

def test_foobar():
    """
    Test the function
    """
    assert do_nothing() == 'bar'
