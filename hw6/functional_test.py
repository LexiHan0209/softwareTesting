import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.close()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://save-a-lot.com/")
        
        elem = driver.find_element_by_name("zipcode")
        elem.send_keys("bbbb")
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        assert "We did not find any results. Try refining your search."  in driver.page_source

        elem = driver.find_element_by_name("smartfield")
        elem.send_keys("aaaa")
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        assert "We did not find any results. Try refining your search."  in driver.page_source


if __name__ == "__main__":
    unittest.main()
