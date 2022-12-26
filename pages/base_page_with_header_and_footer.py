import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class PageWithHeaderAndFooter(BasePage):
    """Top menu bar - The bar that appears on the top of the page prior to login """

    _PRIMARY_PHONE_LINK = (By.CSS_SELECTOR, "#h-phones-phone1>a")
    _SECONDARY_PHONE_LINK = (By.CSS_SELECTOR, "#h-phones-phone2>a")

    _CART_LINK = (By.ID, 'h-cart')
    _VISITED_PRODS_LINK = (By.CSS_SELECTOR, "a[href$='visited.html']")

    _RULES_LINK = (By.CSS_SELECTOR, 'a[href*="pravila-raboty_article.html"]')
    _PERSONAL_DATA_POLICY = (By.CSS_SELECTOR, 'a[href*="politika-obrabotki-personalnyh-dannyh_article.html"]')

    _LOGIN_LINK = (By.CSS_SELECTOR, 'a[href*="account_login.html"]')
    _REGISTRATION_LINK = (By.CSS_SELECTOR, 'a[href*="account_register.html"]')
    _FAVORITES_LINK = (By.CSS_SELECTOR, 'a[href*="favorites.html"]')

    _MOBILE_VERSION_LINK = (By.XPATH, "//a[text()='МОБ. ВЕРСИЯ']")
    _DELIVERY_PAGE_LINK = (By.XPATH, "//a[text()='ДОСТАВКА']")
    _GUARANTEE_PAGE_LINK = (By.XPATH, "//a[text()='ГАРАНТИЯ']")
    _CREDIT_PAGE_LINK = (By.XPATH, "//a[text()='КРЕДИТ']")
    _COOPERATION_PROGRAM_PAGE_LINK = (By.XPATH, "//a[text()='СОТРУДНИЧЕСТВО']")
    _FORUM_PAGE_LINK = (By.XPATH, "//a[text()='ФОРУМ']")
    _WHOLESALE_LEG_PERSON_PAGE_LINK = (By.XPATH, "//a[text()='ОПТ / ЮР. ЛИЦАМ']")
    _REGIONS_PAGE_LINK = (By.XPATH, "//a[text()='РЕГИОНЫ РФ']")

    _CUSTOMER_ACCOUNT_LINK = (By.XPATH, "//a[contains(@href, 'account.html')]")

    _CALL_TO_MANAGER_WORKING_HOURS = (By.CSS_SELECTOR, ".h-phones-num")

    _EXT1_DELIVERY_RESERVE_TIME_INTERVAL = (By.XPATH, "//span[text()='доставка/резерв']/../span[2]")
    _EXT2_WAREHOUSE_CASH_REGIONS_TIME_INTERVAL = (By.XPATH, "//span[text()='опт, безнал, регионы']/../span[2]")
    _EXT3_GUARANTEE_TIME_INTERVAL = (By.XPATH, "//span[text()='гарантия']/../span[2]")
    _EXT4_CREDIT_DEP_TIME_INTERVAL = (By.XPATH, "//span[text()='кредитный отдел']/../span[2]")

    _EXT1_LINK = (By.XPATH, "(//div[@class='h-info-text'])[1]//a")
    _EXT2_LINK = (By.XPATH, "(//div[@class='h-info-text'])[2]//a")
    _EXT3_LINK = (By.XPATH, "(//div[@class='h-info-text'])[3]//a")
    _EXT4_LINK = (By.XPATH, "(//div[@class='h-info-text'])[4]//a")

    _CREDIT_HELP_POPUP = (By.ID, "creditHelp_popup")

    @allure.step("Получить главный телефон")
    def get_primary_phone_text(self):
        return self.get_text(self._PRIMARY_PHONE_LINK)

    @allure.step("Получить второй телефон")
    def get_secondary_phone_text(self):
        return self.get_text(self._SECONDARY_PHONE_LINK)

    @allure.step("Открываем ссылку на правила работы")
    def open_rules_link(self):
        self.click(self._RULES_LINK)

    @allure.step("Ищем ссылку на Политику обработки персональных данных")
    def personal_data_policy_link(self):
        self.click(self._PERSONAL_DATA_POLICY)

    @allure.step("Ищем кнопку корзины")
    def cart_link(self):
        self.click(self._CART_LINK)

    @allure.step("Ищем кнопку Вы смотрели")
    def visited_prods_button(self):
        self.click(self._VISITED_PRODS_LINK)

    @allure.step("Ищем кнопку Мобильная версия в навбаре")
    def mobile_version_link_is_visible(self):
        return self.is_locator_displayed(self._MOBILE_VERSION_LINK)


    @allure.step("Ищем кнопку Доставка в навбаре")
    def delivery_link_is_visible(self):
        return self.is_locator_displayed(self._DELIVERY_PAGE_LINK)

    @allure.step("Ищем кнопку Гарантия в навбаре")
    def guarantee_link_is_visible(self):
        return self.is_locator_displayed(self._GUARANTEE_PAGE_LINK)

    @allure.step("Ищем кнопку Кредит в навбаре")
    def credit_link_is_visible(self):
        return self.is_locator_displayed(self._CREDIT_PAGE_LINK)

    @allure.step("Ищем кнопку Сотрудничество в навбаре")
    def cooperation_link_is_visible(self):
        return self.is_locator_displayed(self._COOPERATION_PROGRAM_PAGE_LINK)

    @allure.step("Ищем кнопку Форум в навбаре")
    def forum_link_is_visible(self):
        return self.is_locator_displayed(self._FORUM_PAGE_LINK)

    @allure.step("Ищем кнопку Опт/Юр.лицам в навбаре")
    def wholesale_leg_person_link_is_visible(self):
        return self.is_locator_displayed(self._WHOLESALE_LEG_PERSON_PAGE_LINK)

    @allure.step("Ищем кнопку Регионы РФ в навбаре")
    def regions_link_is_visible(self):
        return self.is_locator_displayed(self._REGIONS_PAGE_LINK)

    @allure.step("Получение рабочих часов в Назовите менеджеру № товара")
    def call_to_manager_time_interval(self):
        return self.get_text(self._CALL_TO_MANAGER_WORKING_HOURS)

    @allure.step("Получение рабочих часов в Доб.1")
    def ext1_get_time_interval(self):
        return self.get_text(self._EXT1_DELIVERY_RESERVE_TIME_INTERVAL)

    @allure.step("Клик на ссылке Доб.1")
    def ext1_link_click(self):
        self.click(self._EXT1_LINK)

    @allure.step("Получение рабочих часов в Доб.2")
    def ext2_get_time_interval(self):
        return self.get_text(self._EXT2_WAREHOUSE_CASH_REGIONS_TIME_INTERVAL)

    @allure.step("Клик на ссылке Доб.2")
    def ext2_link_click(self):
        self.click(self._EXT2_LINK)

    @allure.step("Получение рабочих часов в Доб.3")
    def ext3_get_time_interval(self):
        return self.get_text(self._EXT3_GUARANTEE_TIME_INTERVAL)

    @allure.step("Клик на ссылке Доб.3")
    def ext3_link_click(self):
        self.click(self._EXT3_LINK)

    @allure.step("Получение рабочих часов в Доб.4")
    def ext4_get_time_interval(self):
        return self.get_text(self._EXT4_CREDIT_DEP_TIME_INTERVAL)

    @allure.step("Клик на ссылке Доб.4")
    def ext4_link_click(self):
        self.click(self._EXT4_LINK)

    @allure.step("Проверяем, что поп-ап с инфой о кредите показывается")
    def online_credit_popup_is_visible(self):
        return self.is_locator_displayed(self._CREDIT_HELP_POPUP)

    @allure.step("Нажимаем кнопку Регистрации")
    def registration_link_click(self):
        return self.click(self._REGISTRATION_LINK)

    @allure.step("Нажимаем кнопку Логин")
    def login_link_click(self):
        return self.click(self._LOGIN_LINK)

    @allure.step("Ищем Клиент №")
    def check_if_customer_account_link_is_present(self):
        return self.is_locator_displayed(self._CUSTOMER_ACCOUNT_LINK)

    @allure.step("Проверяем наличие ссылки на Избранное")
    def check_if_favorites_link_is_present(self):
        return self.is_locator_displayed(self._FAVORITES_LINK)
