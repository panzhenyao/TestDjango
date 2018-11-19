from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        self.assertIn('To-Do',self.browser.title)
        head_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',head_text)

        #应用邀请她输入一个代办事项
        inputbox=self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        #她在一个文本框中输入了'Buy peacock featheers'
        #伊迪丝的爱好是使用假蝇做鱼饵钓鱼
        inputbox.send_keys('Buy peacock feathers')

        #她按回车建后，页面更新了
        #待办事项表格中显示了’1：Buy peacock feathers‘
        inputbox.send_keys(Keys.ENTER)

        table =self.browser.find_element_by_id('id_list_table')
        rows =table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1:Buy peacock feathers ' for row in rows)

        )
        #页面中又显示了一个文本框 ，可以输入其他的待办事项
        #她输入了’Use peacock feathers to make a fly‘
        #伊迪丝做事很有条理
        self.fail('Finsh the tests!')

if __name__ == '__main__' :
    unittest.main(warnings='ignore')

