from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BaseElement(object):
    def __init__(self, driver, value, by):
        self.driver = driver
        self.value = value
        self.by = by
        self.locator = (self.by, self.value)

        self.web_element = None
        self.find()

    def find(self):
        try:
            element = WebDriverWait(self.driver, 5).until(
                expected_conditions.visibility_of_element_located(locator=self.locator))
            self.web_element = element
            return True
        except TimeoutException:
            return None

    def input_text(self, text):
        self.web_element.clear()
        self.web_element.send_keys(text)
        return None

    def click(self):
        element = WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(locator=self.locator),
            message='Element is not clickable.'
        )
        element.click()
        return None

    def attribute(self, attr_name):
        attribute = self.web_element.get_attribute(attr_name)
        return attribute

    def text(self):
        text = self.web_element.text
        return text
