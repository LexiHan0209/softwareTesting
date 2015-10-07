from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def test_that_toasters_appear_in_search_at_correct_price_and_rating(browser):
	# Customer goes to Google
	browser.get("http://www.google.com")
	assert "Google" in browser.title	
	
	# customer enters "coffee maker" in the search box
	search_box = browser.find_element_by_name("q")
	search_box.send_keys("coffee makers")
	search_box.send_keys(Keys.RETURN)
	
	# amazon appears in the first page of results
	browser.implicitly_wait(4)
	results = browser.find_element_by_id("ires")
	targets = results.find_elements_by_tag_name("a")
	link = None
	for target in targets:
		if target.get_attribute("href").startswith("http://www.amazon.com"):
			link = target.get_attribute("href")
	assert link != None
		
	# Customer clicks the amazon link
	browser.get(link)
	browser.implicitly_wait(4)
	assert "Amazon" in browser.title	
	
	# Page of coffee makers appears
	assert "coffee makers" in browser.page_source
	
	# Our coffee makers is on the page
	assert "Hamilton" in browser.page_source
	items = browser.find_elements_by_class_name("celwidget")
	hamilton_item = None
	position = 0
	n = 0
	for item in items:
		n = n + 1
		if "Hamilton" in item.text:
			hamilton_item = item 
			position = n
			break
	assert hamilton_item != None
	
	# hamilton_item is in the top 10
	assert position <= 10

	# Our hamilton_item is less than $100.00
	text = hamilton_item.text
	lowest_price = 10000000000000.00
	for line in text.split("\n"):
		if line.startswith("$"):
			line = line.replace("$","")
			if " " in line:
				line = line.split(" ")[0]
			value = float(line)
			if value < lowest_price:
				lowest_price = value
	assert lowest_price < 100.00		

	# Customer searches for 12-cup on that page
	search_box = browser.find_element_by_id("twotabsearchtextbox")
	search_box.send_keys("coffee makers 12-cup")
	search_box.send_keys(Keys.RETURN)

	# Our hamilton is one of the top 2 results
	assert "Hamilton" in browser.page_source
	items = browser.find_elements_by_class_name("celwidget")
	hamilton_item = None
	position = 0
	n = 0
	for item in items:
		n = n + 1
		if "Hamilton" in item.text:
			hamilton_item = item 
			position = n
			break
	assert hamilton_item != None
	
	# HAMILTON is in the top 2
	assert position <= 2

	# Our 4-slice toaster gets review of 4 stars or higher
	#star_items = oster_item.find_elements_by_class_name("a-icon-star")
	#for star_item in star_items:
	#	print(star_item.text)

	#print("pass")


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors","test-type"])
options.add_argument("--start-maximized")
options.add_argument('--disable-application-cache')
browser = webdriver.Chrome(chrome_options=options)

test_that_toasters_appear_in_search_at_correct_price_and_rating(browser)

time.sleep(3)

#browser.close()	

#driver = webdriver.Firefox()
#driver.get("http://www.python.org")
#assert "Python" in driver.title
#elem = driver.find_element_by_name("q")
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()
