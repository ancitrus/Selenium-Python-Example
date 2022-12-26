import allure
from selenium.webdriver.common.by import By

from pages.base_page_with_header_and_footer import PageWithHeaderAndFooter


class IndexPage(PageWithHeaderAndFooter):
    _PRIMARY_PHONE_LINK = (By.XPATH, "(//a[contains(@class, 'header-block-phone__link')])[1]")
    _SECONDARY_PHONE_LINK = (By.XPATH, "(//a[contains(@class, 'header-block-phone__link')])[2]")

    CONTACTS_PAGE_LINK = (By.XPATH, "//li[not(contains(@class, 'nav-main__item--mobile'))]"
                                    "/a[contains(@href,'contacts_article.html')]")
    _CART_LINK = (By.XPATH, "//*[contains(@class,'fa-shopping-cart')]/parent::a")

    _MOBILE_VERSION_LINK = (By.CSS_SELECTOR, ".nav-main__item--desktop > a")
    _DELIVERY_PAGE_LINK = (By.XPATH, "//li[not(contains(@class, 'nav-main__item--mobile'))]"
                                     "/a[contains(@href,'dostavka_article.html')]")
    _GUARANTEE_PAGE_LINK = (By.XPATH, "//li[not(contains(@class, 'nav-main__item--mobile'))]"
                                      "/a[contains(@href,'ya200sell_article.html')]")
    _CREDIT_PAGE_LINK = (By.XPATH, "//li[not(contains(@class, 'nav-main__item--mobile'))]"
                                   "/a[contains(@href,'credit_article.html')]")
    _COOPERATION_PROGRAM_PAGE_LINK = (By.XPATH, "//li[not(contains(@class, 'nav-main__item--mobile'))]"
                                                "/a[contains(@href,'sotrudnichestvo_article.html')]")
    _DISCOUNTS_PAGE_LINK = (By.XPATH, "//li[not(contains(@class, 'nav-main__item--mobile'))]"
                                      "/a[contains(@href,'akcii-i-specpredlozhenia_article.html')]")
    _FORUM_PAGE_LINK = (By.XPATH, "//li[not(contains(@class, 'nav-main__item--mobile'))]"
                                  "/a[contains(@href,'//player.ru/talk/?from_shop')]")
    _WHOLESALE_LEG_PERSON_PAGE_LINK = (By.XPATH, "//li[not(contains(@class, 'nav-main__item--mobile'))]"
                                                 "/a[contains(@href,'optoviy-otdel_article.html')]")
    _REGIONS_PAGE_LINK = (By.XPATH, "//li[not(contains(@class, 'nav-main__item--mobile'))]"
                                    "/a[contains(@href,'regions_article.html')]")

    _CALL_TO_MANAGER_WORKING_HOURS = (By.CSS_SELECTOR, ".header-block__caption")

    _EXT1_DELIVERY_RESERVE_TIME_INTERVAL = (By.XPATH, "//a[text()='доставка / резерв']/../span")
    _EXT2_WAREHOUSE_CASH_REGIONS_TIME_INTERVAL = (By.XPATH, "//a[text()='опт, безнал, регионы РФ']/../span")
    _EXT3_GUARANTEE_TIME_INTERVAL = (By.XPATH, "//a[text()='помощь в гарантии']/../span")
    _EXT4_CREDIT_DEP_TIME_INTERVAL = (By.XPATH, "//a[text()='кредитный отдел']/../span")

    _EXT1_LINK = (By.XPATH, "(//dl[@class='header-block-phone__info'])[1]//a")
    _EXT2_LINK = (By.XPATH, "(//dl[@class='header-block-phone__info'])[2]//a")
    _EXT3_LINK = (By.XPATH, "(//dl[@class='header-block-phone__info'])[3]//a")
    _EXT4_LINK = (By.XPATH, "(//dl[@class='header-block-phone__info'])[4]//a")

    _FAVORITES_LINK = (By.XPATH, "//a[contains(@href,'favorites.html') and contains(@class, 'header-top__link')]")

    @allure.step("Нажимаем кнопку Контакты в навбаре на index page")
    def contacts_link_click(self):
        return self.click(self.CONTACTS_PAGE_LINK)

    @allure.step("Ищем кнопку Скидки в навбаре на index page")
    def discounts_link_is_visible(self):
        return self.is_locator_displayed(self._DISCOUNTS_PAGE_LINK)

