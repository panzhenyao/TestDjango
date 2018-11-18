from django.test import TestCase
from .views import home_page
from django.core.urlresolvers import resolve
# Create your tests here.
class HomePageTest(TestCase):
    '''单元测试'''
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve( '/' )
        self.assertEqual(found.func, home_page)
