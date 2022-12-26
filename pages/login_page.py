import allure
from selenium.webdriver.common.by import By

from pages.registration_page import RegistrationPage


class LoginPage(RegistrationPage):
    """ Локаторы """
    _LOGIN_FIELD = (By.ID, "p_login")
    _PASSWORD_FIELD = (By.ID, "p_pass")
    _ENTER_BUTTON = (By.CSS_SELECTOR, ".account_form_buttons.right > .green_button_small")
    _LOGIN_ERROR = (By.CLASS_NAME, "error_text")

    @allure.step("Заполнение формы логина")
    def fill_login_form(self, login: str, password: str):
        self.fill_text(self._LOGIN_FIELD, login)
        self.fill_text(self._PASSWORD_FIELD, password)
        self.click(self._ENTER_BUTTON)

    @allure.step("Проверка наличия сообщения об ошибке логина пользователя")
    def check_login_error_message_is_present(self):
        return self.is_locator_displayed(self._LOGIN_ERROR)


