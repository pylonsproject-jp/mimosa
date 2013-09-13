import unittest
import webtest

class TestDemo(unittest.TestCase):
    def _makeAUT(self):
        import basic
        return webtest.TestApp(basic.application)

    def test_fn(self):
        app = self._makeAUT()
        app.get('/')
