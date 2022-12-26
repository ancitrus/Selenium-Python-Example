import allure
from selenium.webdriver.common.by import By

from pages.base_page_with_header_and_footer import PageWithHeaderAndFooter


class StaticPage(PageWithHeaderAndFooter):
    _PAGE_HEADER = (By.CSS_SELECTOR, ".block_header")

    @allure.step("Получить заголовок страницы (оранжевая плашка)")
    def get_page_header(self):
        return self.get_text(self._PAGE_HEADER)
