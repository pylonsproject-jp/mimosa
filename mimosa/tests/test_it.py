from pyramid import testing
import unittest

class TestIndex(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def _callFUT(self, *args, **kwargs):
        from mimosa.views import index
        return index(*args, **kwargs)

    def test_index(self):
        request = testing.DummyRequest()
        result = self._callFUT(request)
        self.assertEqual(result, {})
