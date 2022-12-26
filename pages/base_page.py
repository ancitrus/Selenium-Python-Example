import allure
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert


class BasePage:
    """ Wrapper for selenium operations """

    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 10)

    def click(self, webelement):
        el = self._wait.until(expected_conditions.element_to_be_clickable(webelement))
        self._highlight_element(el, "green")
        el.click()
        self._driver.switch_to.window(self._driver.window_handles[-1])

    def fill_text(self, webelement, txt):
        el = self._wait.until(expected_conditions.element_to_be_clickable(webelement))
        el.clear()
        self._highlight_element(el, "green")
        el.click()
        el.send_keys(txt)

    def clear_text(self, webelement):
        el = self._wait.until(expected_conditions.element_to_be_clickable(webelement))
        el.clear()

    def scroll_to_bottom(self):
        self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def submit(self, webelement):
        self._highlight_element(webelement, "green")
        webelement.submit()

    def get_text(self, webelement):
        el = self._wait.until(expected_conditions.visibility_of_element_located(webelement))
        self._highlight_element(el, "green")
        return el.text

    def move_to_element(self, webelement):
        action = ActionChains(self._driver)
        self._wait.until(expected_conditions.visibility_of(webelement))
        action.move_to_element(webelement).perform()

    @allure.step("Ищем элемент по локатору и проверяем его видимость")
    def is_locator_displayed(self, locator):
        try:
            webelement = self._driver.find_element(*locator)
            return self._is_elem_displayed(webelement)
        except StaleElementReferenceException:
            return False
        except NoSuchElementException:
            return False

    def is_alert_displayed(self, dismiss=False):
        try:
            self._wait.until(expected_conditions.alert_is_present())
        except TimeoutException:
            return False
        else:
            if dismiss:
                self.alert_dismiss()
            return True

    def is_checkbox_checked(self, webelement):
        el = self._wait.until(expected_conditions.element_to_be_clickable(webelement))
        if not el.aria_role == 'checkbox':
            raise Exception('This is not checkbox')
        self._highlight_element(el, "green")
        if not el.get_property('checked'):
            return False
        else:
            return True

    def alert_accept(self):
        Alert(self._driver).accept()

    def alert_dismiss(self):
        Alert(self._driver).dismiss()

    def alert_send_keys(self, keys_to_send):
        Alert(self._driver).send_keys(keys_to_send)

    def alert_get_text(self):
        return Alert(self._driver).text

    def checkbox_checked(self, webelement, checked=True):
        el = self._wait.until(expected_conditions.element_to_be_clickable(webelement))
        if not el.aria_role == 'checkbox':
            raise Exception('This is not checkbox')
        self._highlight_element(el, "green")
        if checked:
            if not el.get_property('checked'):
                el.click()
        else:
            if el.get_property('checked'):
                el.click()
        self._driver.switch_to.window(self._driver.window_handles[-1])

    def _highlight_element(self, webelement, color):
        original_style = webelement.get_attribute("style")
        new_style = f"background-color:yellow;border: 1px solid {color}{original_style}"
        self._driver.execute_script(
            "var tmpArguments = arguments;setTimeout(function () {tmpArguments[0].setAttribute('style', '"
            + new_style + "');},0);", webelement)
        self._driver.execute_script(
            "var tmpArguments = arguments;setTimeout(function () {tmpArguments[0].setAttribute('style', '"
            + original_style + "');},400);", webelement)

    def _is_elem_displayed(self, webelement):
        return webelement.is_displayed()

    def get_current_url(self):
        return self._driver.current_url
