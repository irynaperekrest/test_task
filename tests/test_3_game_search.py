import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.login_page import LoginPage
from pages.game_search_page import GameSearchPage
from resources.test_data import TestData


class GameSearchTests(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.login_page = LoginPage(self.browser)
        self.login_page.go()
        self.login_page.login(TestData.existing_acc_email, TestData.password)
        WebDriverWait(self.browser, 5).until(lambda a: self.browser.current_url != self.login_page.url)

        self.game_search_page = GameSearchPage(self.browser)
        self.game_search_page.go()

    def test_booster_search(self):

        self.game_search_page.search_button.click()
        self.assertTrue(self.game_search_page.search_input.find())

        self.game_search_page.search_input.input_text(TestData.game_name)
        self.assertTrue(self.game_search_page.get_game_link(TestData.game_name).find())

        self.game_search_page.get_game_link(TestData.game_name).click()
        self.assertEqual(self.browser.current_url, 'https://www.optibet.lv/en/casino/games/booster/playing')

    def tearDown(self):
        self.browser.quit()
