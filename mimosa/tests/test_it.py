from pyramid import testing
import unittest


class TestAddSite(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.config.include("mimosa")

    def tearDown(self):
        testing.tearDown()

    def test_it(self):
        site = testing.DummyModel()
        name = "testing"
        self.config.add_admin_site(site, name)


class TestIndex(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()
        self.config.include("mimosa")

    def tearDown(self):
        testing.tearDown()

    def _callFUT(self, *args, **kwargs):
        from mimosa.views import index
        return index(*args, **kwargs)

    def test_index(self):
        request = testing.DummyRequest()
        result = self._callFUT(request)
        self.assertEqual(result, {})
