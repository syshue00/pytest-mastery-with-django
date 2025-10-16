import pytest
from django.test import LiveServerTestCase
from selenium import webdriver

# Example 1
# class TestBrowser1(LiveServerTestCase):
#     def test_example(self):
#         chromeService = webdriver.ChromeService(executable_path="./chromedriver")
#         driver = webdriver.Chrome(service = chromeService)
#         driver.get(("%s%s" % (self.live_server_url, "/admin/")))
#         assert "Log in | Django site admin" in driver.title

# Example 2
# class TestBrowser2(LiveServerTestCase):
#     def test_example(self):
#         options = webdriver.ChromeOptions()
#         options.add_argument("--headless")
#         chromeService = webdriver.ChromeService(executable_path="./chromedriver")
#         driver = webdriver.Chrome(service=chromeService, options=options)
#         driver.get(("%s%s" % (self.live_server_url, "/admin/")))
#         assert "Log in | Django site admin" in driver.title

# Example 3
# Fixture for Chrome
# @pytest.fixture(scope="class")
# def chrome_driver_init(request):

#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")
#     chromeService = webdriver.ChromeService(executable_path="./chromedriver")
#     chrome_driver = webdriver.Chrome(service=chromeService, options=options)
#     request.cls.driver = chrome_driver
#     yield
#     chrome_driver.close()

# @pytest.mark.usefixtures("chrome_driver_init")
# class Test_URL_Chrome(LiveServerTestCase):
#     def test_open_url(self):
#         self.driver.get(("%s%s" % (self.live_server_url, "/admin/")))
#         assert "Log in | Django site admin" in self.driver.title

# @pytest.fixture(params=["chrome", "firefox"], scope="class")
# def driver_init(request):
#     if request.param == "chrome":
#         options = webdriver.ChromeOptions()
#         options.add_argument("--headless")
#         chrome_service = webdriver.ChromeService(executable_path="./chromedriver")
#         web_driver = webdriver.Chrome(service=chrome_service, options=options)
#     if request.param == "firefox":
#         options = webdriver.FirefoxOptions()
#         options.add_argument("--headless")
#         firefox_service = webdriver.FirefoxService(executable_path="./geckodriver")
#         web_driver = webdriver.Firefox(service=firefox_service, options=options)
#     request.cls.driver = web_driver
#     yield
#     web_driver.close()

@pytest.mark.usefixtures("driver_init")
class Test_URL_Chrome:
    def test_open_url(self, live_server):
        self.driver.get(("%s%s" % (live_server.url, "/admin/")))
        assert "Log in | Django site admin" in self.driver.title
