import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.static_page_with_header_and_footer import StaticPage


class RegistrationPage(StaticPage):
    """ Локаторы """
    _FULL_NAME_FIELD = (By.ID, "p_fio")
    _EMAIL_FIELD = (By.ID, "p_email")
    _PHONE_FIELD = (By.ID, "p_tel")
    _DOB_FIELD = (By.ID, "p_birthday")
    _CHECKBOX_FIELD = (By.ID, "rpop_clientrulesconfirm")
    _LINK_IN_DETAIL = (By.CSS_SELECTOR, "a[href='./pravila-raboty_article.html']")
    _REGISTRATION_BUTTON = (By.CLASS_NAME, "green_button_small")
    _REGISTRATION_ERROR = (By.CLASS_NAME, "error_text")
    _REGISTRATION_GOOD = (By.CLASS_NAME, "good_text")

    @allure.step("Проверка наличия полей и элементов")
    def check_if_all_elements_are_present(self):
        return all([
            self.is_locator_displayed(self._FULL_NAME_FIELD),
            self.is_locator_displayed(self._EMAIL_FIELD),
            self.is_locator_displayed(self._PHONE_FIELD),
            self.is_locator_displayed(self._DOB_FIELD),
            self.is_locator_displayed(self._CHECKBOX_FIELD),
            self.is_locator_displayed(self._LINK_IN_DETAIL),
            self.is_locator_displayed(self._REGISTRATION_BUTTON),
        ]);
    @allure.step("Проверка, что чекбокс при загрузке страницы отмечен")
    def is_checkbox_checked_on_page_load(self):
        return self.is_checkbox_checked(self._CHECKBOX_FIELD)

    @allure.step("Заполнение и отправка формы регистрации")
    def fill_register_form(self, name: str, email: str, phone: str, dob: str, checkbox_checked: bool):
        self.fill_text(self._FULL_NAME_FIELD, name)
        self.fill_text(self._EMAIL_FIELD, email)
        self.fill_text(self._PHONE_FIELD, phone)
        self.fill_text(self._DOB_FIELD, dob)
        self.checkbox_checked(self._CHECKBOX_FIELD, checkbox_checked)
        self.click(self._REGISTRATION_BUTTON)

    @allure.step("Проверка наличия сообщения об ошибке регистрации пользователя")
    def check_registration_error_is_present(self):
        return self.is_locator_displayed(self._REGISTRATION_ERROR)

    @allure.step("Проверка наличия сообщения об успешной регистрации пользователя")
    def check_registration_success_message_is_present(self):
        return self.is_locator_displayed(self._REGISTRATION_GOOD)
