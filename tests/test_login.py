import allure
import pytest
from assertpy import assert_that
from faker import Faker

from pages.login_page import LoginPage
from tests.test_base import BaseTest

fake = Faker('ru_RU')

wrong_login_data = [
    (fake.word(), fake.word())
]


@allure.severity(allure.severity_level.CRITICAL)
@allure.epic("Security")
@allure.feature("Login")
class TestLogin(BaseTest):

    @allure.step("Заходим на страницу логина")
    @pytest.fixture(autouse=True)
    def go_to_login_page(self, injector):
        self.pages.index.login_link_click()
        self.test_page: LoginPage = self.pages.login

    @allure.title("Проверка наличия всех полей")
    @allure.description("Проверка, что все поля формы логин присутствуют")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.dependency(name="test_all_login_form_fields_are_present")
    def test_all_login_form_fields_are_present(self):
        assert_that(self.test_page.check_if_all_elements_are_present()) \
            .described_as('Все поля формы на месте') \
            .is_true()

    @allure.title("Логин несуществующего пользователя")
    @allure.description("Проверка наличия сообщения об ошибке, если пользователь не найден")
    @pytest.mark.parametrize("login, password", wrong_login_data)
    @pytest.mark.dependency(name="test_wrong_login", depends=["test_all_login_form_fields_are_present"])
    @allure.severity(allure.severity_level.NORMAL)
    def test_wrong_login(self, login, password):
        self.test_page.fill_login_form(login, password)
        assert_that(self.test_page.check_login_error_message_is_present()).is_true()

    @allure.title("Логин пользователя")
    @allure.description("Логин существующего пользователя")
    @pytest.mark.dependency(name="test_login", depends=["test_all_login_form_fields_are_present"])
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login(self):
        self.test_page.fill_login_form(
            self.config_reader.config_section_dict("Login data")["login"],
            self.config_reader.config_section_dict("Login data")["password"])
        assert_that(self.test_page.get_current_url()).is_equal_to(
            self.config_reader.config_section_dict("Base Url")["base_url"]
        )
        self.test_page = self.pages.index
        assert_that(self.test_page.check_if_customer_account_link_is_present()).is_true()
        assert_that(self.test_page.check_if_favorites_link_is_present()).is_true()
