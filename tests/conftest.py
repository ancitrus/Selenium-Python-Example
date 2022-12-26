from datetime import datetime

import allure
import requests
from fake_useragent import UserAgent
from git import Repo
from pytest import fixture, hookimpl
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from globals.dir_global import ROOT_DIR
from pages.base_page_with_header_and_footer import PageWithHeaderAndFooter
from pages.cart_page import CartPage
from pages.contacts_page import ContactsPage
from pages.data_policy_page import PersonalDataPolicyPage
from pages.delivery_page import DeliveryPage
from pages.digital_electronics_delivery_page import DigitalElectronicsDeliveryPage
from pages.digital_electronics_page import DigitalElectronicsPage
from pages.index_page import IndexPage
from pages.login_page import LoginPage
from pages.okp_page import OKPPage
from pages.rules_page import RulesPage
from pages.static_page_with_header_and_footer import StaticPage
from pages.visited_prods_page import VisitedProdsPage
from pages.registration_page import RegistrationPage
from utils.config_parser import AllureEnvironmentParser
from utils.config_parser import ConfigParserIni

UA_STRING_FOR_CAPTCHA = "AncitrusTest"


# reads parameters from pytest command line
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser that the automation will run in")


def get_public_ip():
    return requests.get("http://checkip.amazonaws.com").text.rstrip()


@fixture(scope="session")
def prep_properties():
    return ConfigParserIni("props.ini")


@fixture(autouse=True, scope="session")
# fetch browser type and base url then writes a dictionary of key-value pair into allure's environment.properties file
def write_allure_environment(prep_properties):
    yield
    repo = Repo(ROOT_DIR)
    env_parser = AllureEnvironmentParser("environment.properties")
    env_parser.write_to_allure_env(
        {
            "Browser": driver.name,
            "Driver_Version": driver.capabilities['browserVersion'],
            "Base_URL": base_url,
            "Commit_Date": datetime.fromtimestamp(repo.head.commit.committed_date).strftime('%c'),
            "Commit_Author_Name": repo.head.commit.author.name,
            "Branch": repo.active_branch.name
        })


@fixture
# Instantiates Page Objects
def pages():
    class PagesRepository:
        def __init__(self, _driver):
            self.index: PageWithHeaderAndFooter = IndexPage(_driver)
            self.contacts: StaticPage = ContactsPage(_driver)
            self.delivery: StaticPage = DeliveryPage(_driver)
            self.rules: StaticPage = RulesPage(_driver)
            self.personal_data_policy: StaticPage = PersonalDataPolicyPage(_driver)
            self.cart: StaticPage = CartPage(_driver)
            self.visited_prods: StaticPage = VisitedProdsPage(_driver)
            self.okp: StaticPage = OKPPage(_driver)
            self.digital_electronics: StaticPage = DigitalElectronicsPage(_driver)
            self.digital_electronics_delivery: StaticPage = DigitalElectronicsDeliveryPage(_driver)
            self.registration: StaticPage = RegistrationPage(_driver)
            self.login: RegistrationPage = LoginPage(_driver)

    return PagesRepository(driver)


@fixture(autouse=True)
def create_driver(write_allure_environment, prep_properties, request):
    global browser, base_url, driver
    browser = request.config.option.browser
    base_url = prep_properties.config_section_dict("Base Url")["base_url"]
    ua = UserAgent()

    # browser = "chrome_headless"

    if browser == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.set_preference("general.useragent.override", f'{ua["firefox"]}[{UA_STRING_FOR_CAPTCHA}]')
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
    elif browser == "safari":
        driver = webdriver.Safari()
    elif browser == "chrome_headless" or browser == "chrome-headless":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f'user-agent={ua["chrome"]}(headless)[{UA_STRING_FOR_CAPTCHA}]')
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    else:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f'user-agent={ua["chrome"]}[{UA_STRING_FOR_CAPTCHA}]')
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get(base_url)
    yield
    if request.node.rep_call.failed:
        screenshot_name = f"screenshot on failure: {datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}"
        allure.attach(body=driver.get_screenshot_as_png(), name=screenshot_name,
                      attachment_type=allure.attachment_type.PNG)
        allure.attach(body=get_public_ip(), name="public ip address", attachment_type=allure.attachment_type.TEXT)
    driver.quit()


@hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, f"rep_{rep.when}", rep)
