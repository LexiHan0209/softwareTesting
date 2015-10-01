import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.close()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.amazon.com")
        self.assertIn("Amazon", driver.title)
        elem = driver.find_element_by_name("field-keywords")
        elem.send_keys("laptop steering wheel desk")
        elem.send_keys(Keys.RETURN)
        assert "Cutequeen Trading car 1pcs Eating/Laptop Steering Wheel Desk Black(pack of 1)"  in driver.page_source

if __name__ == "__main__":
    unittest.main()
