from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    '''功能测试'''
    def setUp(self):
        '''打开浏览器'''
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3) #延迟等待

    def tearDown(self):
        '''关闭浏览器'''
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        '''测试内容'''
        self.browser.get('http://localhost:8000')
        self.assertIn('To-Do lists',self.browser.title)
        self.fail('Finsh the tests!')

if __name__ == '__main__' :
    unittest.main(warnings='ignore')

