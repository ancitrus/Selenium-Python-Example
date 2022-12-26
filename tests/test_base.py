import allure
import pytest

# https://stackoverflow.com/questions/63292928/add-pytest-fixtures-to-a-test-class-using-dependency-injection
# /63436993#63436993
from utils.excel_parser import ExcelParser
from utils.json_parser import JsonParser


class BaseTest:
    @pytest.fixture(autouse=True)
    def injector(self, pages, prep_properties):
        # instantiates pages object, and data readers
        self.pages = pages
        self.test_page = self.pages.index
        self.json_reader = JsonParser("tests_data.json")
        self.config_reader = prep_properties
        self.excel_reader = ExcelParser("data.xls")

    @pytest.fixture(params=['index', pytest.param('contacts')])  # pytest.param('delivery', marks=pytest.mark.skip)
    def on_both_design(self, request):
        if request.param != 'index':
            with allure.step('Переход к странице со старым дизайном'):
                if request.param == 'contacts':
                    self.pages.index.click(self.pages.index.CONTACTS_PAGE_LINK)
                if request.param == 'delivery':
                    self.pages.index.click(self.pages.index.DELIVERY_PAGE_LINK)

                self.test_page = getattr(self.pages, request.param)


