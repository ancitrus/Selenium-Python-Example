import allure
import pytest
from assertpy import assert_that
from faker import Faker

from pages.registration_page import RegistrationPage
from tests.test_base import BaseTest

fake = Faker('ru_RU')

registration_data = [
    ("Test Ancitrus", fake.free_email(), "9008007766", "25.01.1999")
]

existed_user = [
    ("Test Ancitrus", "ancitrus+testpleer@gmail.com", "9008007766", "25.01.1999")
]

registration_data_missed_required = [
    ("", fake.free_email(), fake.random_int(1000000000, 9999999999), "25.01.1999", True),
    (fake.name(), "", fake.random_int(1000000000, 9999999999), "25.01.1999", True),
    (fake.name(), fake.free_email(), "", "25.01.1999", True),
    (fake.name(), fake.free_email(), fake.random_int(1000000000, 9999999999), "25.01.1999", False),
]


@allure.severity(allure.severity_level.CRITICAL)
@allure.epic("Security")
@allure.feature("Register")
class TestRegistration(BaseTest):

    @allure.step("Заходим на страницу регистрации")
    @pytest.fixture(autouse=True)
    def go_to_registration_page(self, injector):
        self.pages.index.registration_link_click()
        self.test_page: RegistrationPage = self.pages.registration

    @allure.title("Проверка наличия всех полей")
    @allure.description("Проверка, что все поля формы присутствуют")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.dependency(name="test_all_fields_are_present")
    def test_all_registration_form_fields_are_present(self):
        assert_that(self.test_page.check_if_all_elements_are_present()) \
            .described_as('Все поля формы на месте') \
            .is_true()

    @allure.title("Проверка чекбокса по-умолчанию")
    @allure.description("Проверка, что при загрузке страницы чекбокс отмечен")
    @pytest.mark.dependency(depends=["test_all_fields_are_present"])
    def test_checkbox_is_checked_on_page_load(self):
        assert_that(self.test_page.is_checkbox_checked_on_page_load()).is_true()

    @allure.title("Регистрация пользователя")
    @allure.description("Регистрация пользователя")
    @pytest.mark.parametrize("name, email, phone, dob", registration_data)
    @pytest.mark.dependency(name="test_registration", depends=["test_all_fields_are_present"])
    @allure.severity(allure.severity_level.BLOCKER)
    def test_registration(self, name, email, phone, dob):
        self.test_page.fill_register_form(name, email, phone, dob, checkbox_checked=True)
        assert_that(self.test_page.is_alert_displayed(dismiss=True)).is_false()
        assert_that(self.test_page.check_registration_success_message_is_present()).is_true()

    @allure.title("Регистрация пользователя с уже зарегистрированным email")
    @allure.description("Попытка регистрации пользователя с уже зарегистрированным email")
    @pytest.mark.dependency(depends=["test_all_fields_are_present", "test_registration"])
    @pytest.mark.parametrize("name, email, phone, dob", existed_user)
    def test_registration_existed_user_must_fail(self, name, email, phone, dob):
        self.test_page.fill_register_form(name, email, phone, dob, checkbox_checked=True)
        assert_that(self.test_page.check_registration_error_is_present()).is_true()

    @allure.title("Регистрация без обязательного поля")
    @allure.description("Регистрация пользователя без обязательного поля, должен появляться alert")
    @pytest.mark.dependency(depends=["test_all_fields_are_present", "test_registration"])
    @pytest.mark.parametrize("name, email, phone, dob, acceptance", registration_data_missed_required)
    @allure.severity(allure.severity_level.BLOCKER)
    def test_registration_without_checkbox(self, name, email, phone, dob, acceptance):
        self.test_page.fill_register_form(name, email, phone, dob, checkbox_checked=acceptance)
        assert_that(self.test_page.is_alert_displayed(dismiss=True)).is_true()

