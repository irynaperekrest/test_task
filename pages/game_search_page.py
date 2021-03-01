from selenium.webdriver.common.by import By

from pages.base_element import BaseElement
from pages.base_page import BasePage


class GameSearchPage(BasePage):

    url = "https://www.optibet.lv/en/casino/slots"

    @property
    def search_button(self):
        locator = (By.CSS_SELECTOR, "svg[data-role='searchBtn']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def search_input(self):
        locator = (By.CSS_SELECTOR, "input[data-role='searchInput']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    def get_game_link(self, game_name):
        locator = (By.XPATH, f"//img[@alt='{game_name}']/../..")
        return BaseElement(self.driver, by=locator[0], value=locator[1])
