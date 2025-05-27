import unittest
from alumnium import Alumni
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

load_dotenv()
print(dir(Alumni))

class TestSouceDemo(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument("--start-maximized")
        driver = Chrome(options=options)
        driver.get("https://www.saucedemo.com/")
        self.al = Alumni(driver)
        self.login()

    def login(self):

        self.al.check("Page title contains Swag Labs")
        self.al.check("Page contains login containers")
        self.al.do("Type 'standard_user' in username input")
        self.al.do("Type 'secret_sauce' in password input")
        self.al.do("Send a login request")
        self.al.check("Verify that the inventory page has loaded")
        self.al.check("Page contains products containers")
        
    def test_add_cart_products(self):
        self.al.do("Save the name of three products from the list ")
        self.al.do("Add saved products in the shopping cart")
        self.al.do("Click shopping cart button")
        self.al.check("Verify all the products in the shopping cart with the saved name")
        
    def tearDown(self):
        self.al.quit()