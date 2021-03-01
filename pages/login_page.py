from selenium.webdriver.common.by import By

from pages.base_element import BaseElement
from pages.base_page import BasePage


class LoginPage(BasePage):

    url = "https://www.optibet.lv/en/login"

    @property
    def email_input(self):
        locator = (By.CSS_SELECTOR, "input[data-role='loginEmailInput']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def password_input(self):
        locator = (By.CSS_SELECTOR, "input[data-role='password']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def login_button(self):
        locator = (By.CSS_SELECTOR, "button[data-id='login-button']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    def login(self, login, password):
        self.email_input.input_text(login)
        self.password_input.input_text(password)
        self.login_button.click()
