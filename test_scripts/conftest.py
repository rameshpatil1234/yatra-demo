import allure
import pytest
from allure_commons.types import AttachmentType
from pyjavaproperties import Properties
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_tests", attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="class")
def setup(request,browser,url):
    global driver
    chrome_option = webdriver.ChromeOptions()
    firefox_option = webdriver.FirefoxOptions()
    chrome_option.add_argument("--disable-notifications")
    firefox_option.add_argument("--disable-notifications")
    if browser == 'chrome':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_option)
        print('Launched chrome browser')
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_option)
        print('Launched firefox browser')
    elif browser == 'edge':
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        print('Launched edge browser')
    else:
        print("please enter valid browser ")
    driver.maximize_window()
    driver.get(url)
    request.cls.driver = driver
    yield
    driver.close()


#
# def pytest_addoption(parser):
#     parser.addoption("--browser")
#     parser.addoption("--url")
#
#
# @pytest.fixture(scope="class")
# def browser(request):
#     return request.config.getoption("--browser")
#
#
# @pytest.fixture(scope="class")
# def url(request):
#     return request.config.getoption("--url")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")


@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class")
def url(request):
    return request.config.getoption("--url")
