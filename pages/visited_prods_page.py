from selenium.webdriver.common.by import By

from pages.static_page_with_header_and_footer import StaticPage


class VisitedProdsPage(StaticPage):
    _PAGE_HEADER = (By.CSS_SELECTOR, ".list_head")

