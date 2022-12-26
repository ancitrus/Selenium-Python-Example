import allure
import pytest
from assertpy import assert_that

from tests.test_base import BaseTest


@allure.epic("Header")
@allure.story("Тестирования хедера сайта")
@allure.severity(allure.severity_level.NORMAL)
class TestSiteHeader(BaseTest):

    @allure.title("Проверка кнопки Контакты в навбаре на index page")
    @allure.description("Проверяем, что кнопка Контакты есть в навбаре на index page")
    @pytest.mark.run(order=1)
    def test_contacts_link(self):
        self.test_page.contacts_link_click()
        page = self.pages.contacts
        assert_that(page.get_page_header()).matches('Контакты Плеер.Ру')

    @allure.title("Проверка телефонов")
    @allure.description("Проверяем, что оба телефона отображаются правильно")
    def test_phones_is_visible(self, on_both_design):
        primary_phone = self.test_page.get_primary_phone_text()
        secondary_phone = self.test_page.get_secondary_phone_text()
        assert_that(primary_phone).is_equal_to(self.config_reader.config_section_dict("Pleer phones")['primary'])
        assert_that(secondary_phone).is_equal_to(self.config_reader.config_section_dict("Pleer phones")['secondary'])

    @allure.title("Проверка ссылки на Правила работы, заказа, оплаты и услуг")
    @allure.description("Проверяем, что показывается ссылка на Правила работы, заказа, оплаты и услуг")
    def test_rules_link(self, on_both_design):
        self.test_page.open_rules_link()
        page = self.pages.rules
        assert_that(page.get_page_header()).is_equal_to('Правила работы')

    @allure.title("Проверка ссылки на Политику обработки персональных данных")
    @allure.description("Проверяем, что показывается ссылка на Политику обработки персональных данных")
    def test_personal_data_policy_link(self, on_both_design):
        self.test_page.personal_data_policy_link()
        page = self.pages.personal_data_policy
        assert_that(page.get_page_header()).is_equal_to('Политика обработки персональных данных')

    @allure.title("Проверка ссылки на наличие корзины")
    @allure.description("Проверяем, что корзина показывается")
    def test_cart(self, on_both_design):
        self.test_page.cart_link()
        page = self.pages.cart
        assert_that(page.get_page_header()).matches('корзин')

    @allure.title("Проверка кнопки Вы смотрели")
    @allure.description("Проверяем, что кнопка Вы смотрели на месте")
    def test_visited_prods(self, on_both_design):
        self.test_page.visited_prods_button()
        page = self.pages.visited_prods
        assert_that(page.get_page_header()).is_equal_to('Вы смотрели')

    @allure.title("Проверка кнопки Мобильная версия в навбаре")
    @allure.description("Проверяем, что кнопка Мобильная версия есть в навбаре")
    def test_mobile_version_is_visible(self, on_both_design):
        assert_that(self.test_page.mobile_version_link_is_visible()).is_true()

    @allure.title("Проверка кнопки Доставка в навбаре")
    @allure.description("Проверяем, что кнопка Доставка есть в навбаре")
    def test_delivery_link_is_visible(self, on_both_design):
        assert_that(self.test_page.delivery_link_is_visible()).is_true()

    @allure.title("Проверка кнопки Гарантия в навбаре")
    @allure.description("Проверяем, что кнопка Гарантия есть в навбаре")
    def test_guarantee_link_is_visible(self, on_both_design):
        assert_that(self.test_page.guarantee_link_is_visible()).is_true()

    @allure.title("Проверка кнопки Кредит в навбаре")
    @allure.description("Проверяем, что кнопка Кредит есть в навбаре")
    def test_credit_link_is_visible(self, on_both_design):
        assert_that(self.test_page.credit_link_is_visible()).is_true()

    @allure.title("Проверка кнопки Сотрудничество в навбаре")
    @allure.description("Проверяем, что кнопка Сотрудничество есть в навбаре")
    def test_cooperation_program_link_is_visible(self, on_both_design):
        assert_that(self.test_page.cooperation_link_is_visible()).is_true()

    @allure.title("Проверка кнопки Скидки в навбаре")
    @allure.description("Проверяем, что кнопка Сотрудничество есть в навбаре на index page")
    def test_discounts_link_is_visible(self):
        assert_that(self.test_page.discounts_link_is_visible()).is_true()

    @allure.title("Проверка кнопки Форум в навбаре")
    @allure.description("Проверяем, что кнопка Форум есть в навбаре")
    def test_forum_link_is_visible(self, on_both_design):
        assert_that(self.test_page.forum_link_is_visible()).is_true()

    @allure.title("Проверка кнопки Опт/Юр.лицам в навбаре")
    @allure.description("Проверяем, что кнопка Опт/Юр.лицам есть в навбаре")
    def test_wholesale_leg_person_link_is_visible(self, on_both_design):
        assert_that(self.test_page.wholesale_leg_person_link_is_visible()).is_true()

    @allure.title("Проверка кнопки Регионы РФ в навбаре")
    @allure.description("Проверяем, что кнопка Регионы РФ есть в навбаре")
    def test_regions_link_is_visible(self, on_both_design):
        assert_that(self.test_page.regions_link_is_visible()).is_true()

    @allure.title("Проверка интервала времени в Назовите менеджеру № товара")
    @allure.description("Проверка, что время работы отображается корректно")
    def test_call_to_manager_time_interval_is_correct(self, on_both_design):
        time_interval = self.test_page.call_to_manager_time_interval()
        assert_that(time_interval).matches(r'(?:[0-1]?\d|2[0-3]):00 – (?:[0-1]?\d|2[0-3]):00')

    @allure.title("Проверка интервалов времени в Доб.1-2-3-4")
    @allure.description("Проверка, что время работы в Доб.1-2-3-4 отображается корректно")
    def test_ext1_4_time_interval_is_correct(self, on_both_design):
        time_interval = self.test_page.ext1_get_time_interval()
        assert_that(time_interval).matches(r'(?:[0-1]?\d|2[0-3])-(?:[0-1]?\d|2[0-3])$')

        time_interval = self.test_page.ext2_get_time_interval()
        assert_that(time_interval).matches(r'(?:[0-1]?\d|2[0-3])-(?:[0-1]?\d|2[0-3])$')

        time_interval = self.test_page.ext3_get_time_interval()
        assert_that(time_interval).matches(r'(?:[0-1]?\d|2[0-3])-(?:[0-1]?\d|2[0-3])$')

        time_interval = self.test_page.ext4_get_time_interval()
        assert_that(time_interval).matches(r'(?:[0-1]?\d|2[0-3])-(?:[0-1]?\d|2[0-3])$')

    @allure.title("Проверка ссылки в Доб. 1")
    @allure.description("Проверяем, что отображается страница Доставка бытовой и цифровой техники по Москве и области")
    def test_ext1_link(self, on_both_design):
        self.test_page.ext1_link_click()
        page = self.pages.digital_electronics_delivery
        assert_that(page.get_page_header()).is_equal_to('Доставка бытовой и цифровой техники по Москве и области')
    @allure.title("Проверка ссылки в Доб. 2")
    @allure.description("Проверяем, что отображается страница Цифровая и бытовая техника оптом")
    def test_ext2_link(self, on_both_design):
        self.test_page.ext2_link_click()
        page = self.pages.digital_electronics
        assert_that(page.get_page_header()).is_equal_to('Цифровая и бытовая техника оптом')
    @allure.title("Проверка ссылки в Доб. 3")
    @allure.description("Проверяем, что отображается страница Отдел клиентской поддержки")
    def test_ext3_link(self, on_both_design):
        self.test_page.ext3_link_click()
        page = self.pages.okp
        assert_that(page.get_page_header()).is_equal_to('Отдел клиентской поддержки')

    @allure.title("Проверка ссылки в Доб. 4")
    @allure.description("Проверяем, что отображается поп-ап окно с информацией о заявке на кредит")
    def test_ext4_link(self, on_both_design):
        self.test_page.ext4_link_click()
        assert_that(self.test_page.online_credit_popup_is_visible()).is_true()
