from c21server.server import home

def test_home():
    assert home() == "Hello World"
