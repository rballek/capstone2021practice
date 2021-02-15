from c21server.server import do_nothing

def test_foobar():
    assert do_nothing() == 'bar'
