from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page
from django.template.loader import render_to_string

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


    def test_home_page_returns_correct_html(self):
        #request = HttpRequest()  #1
        #response = home_page(request)  #2
        #self.assertTrue(response.content.startswith(b'<html>'))  #3
        #self.assertIn(b'<title>To-Do lists</title>', response.content)  #4
        #self.assertTrue(response.content.endswith(b'</html>'))  #5
        #self.assertTrue(response.content.strip().endswith(b'</html>'))
        #expected_html = render_to_string('home.html')
        #self.assertEqual(response.content.decode(), expected_html)
        # django r当请求一张页面时，Django把请求的metadata数据包装成一个HttpRequest对象，
        #然后Django加载合适的view方法,把这个HttpRequest 对象作为第一个参数传给view方法。
        #任何view方法都应该返回一个HttpResponse对象。
        
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)

        # The render_to_string shortcut takes one required argument – template_name, 
        #which should be the name of the template to load and render (or a list of 
        # template names, in which case Django will use the first template in the list 
        # that exists) – and two optional arguments:

        self.assertIn('A new list item', response.content.decode())
        expected_html = render_to_string(
            'home.html',
            {'new_item_text':  'A new list item'}
        )
        self.assertEqual(response.content.decode(), expected_html)
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

        