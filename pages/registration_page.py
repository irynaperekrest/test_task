from selenium.webdriver.common.by import By

from pages.base_element import BaseElement
from pages.base_page import BasePage


class RegistrationPage(BasePage):

    url = "https://www.optibet.lv/en/signup"

    # Common elements for both registration form pages

    @property
    def close_icon(self):
        locator = (By.CSS_SELECTOR, "div[data-role='closeIcon']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def page_title(self):
        locator = (By.CSS_SELECTOR, "div[data-role='dialogTitle']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def page_text(self):
        locator = (By.CSS_SELECTOR, "div[data-role='dialogText']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    # 1st registration form page elements

    @property
    def email_input(self):
        locator = (By.CSS_SELECTOR, "input[name='email']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def email_error(self):
        locator = (By.XPATH, "//input[@name='email']/../div[@data-role='validationError']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def password_input(self):
        locator = (By.CSS_SELECTOR, "input[name='password']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def password_error(self):
        locator = (By.XPATH, "//input[@name='password']/../div[@data-role='validationError']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def promocode_question(self):
        locator = (By.CSS_SELECTOR, "div[data-role='promoCodeQuestionButton']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def promocode_input(self):
        locator = (By.CSS_SELECTOR, "input[name='promotionCode']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def close_promocode_icon(self):
        locator = (By.CSS_SELECTOR, "div[data-role='closePromotionCode']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def sign_up_btn(self):
        locator = (By.CSS_SELECTOR, "button[data-id='signup-button']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def terms_checkbox(self):
        locator = (By.XPATH, "//input[@name='tnc']/../span[@data-role='checkboxBox']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def promotions_checkbox(self):
        locator = (By.XPATH, "//input[@name='promotions']/../span[@data-role='checkboxBox']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def login_link(self):
        locator = (By.CSS_SELECTOR, "span[class^='goToLoginContent'] > a")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    # 2nd registration form page elements

    @property
    def pin_input(self):
        locator = (By.CSS_SELECTOR, "input[name='code']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def change_email_link(self):
        locator = (By.CSS_SELECTOR, "div[class^='pinFieldDescription'] > a")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def phone_code_dropdown(self):
        locator = (By.CSS_SELECTOR, "div[data-role='additionalPhoneCode']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def phone_input(self):
        locator = (By.CSS_SELECTOR, "input[name='phoneNumber']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def first_name_input(self):
        locator = (By.CSS_SELECTOR, "input[name='firstName']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def last_name_input(self):
        locator = (By.CSS_SELECTOR, "input[name='lastName']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def birth_day_dropdown(self):
        locator = (By.CSS_SELECTOR, "div[data-role='additionalDobDay']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def birth_month_dropdown(self):
        locator = (By.CSS_SELECTOR, "div[data-role='additionalDobMonth']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def birth_year_dropdown(self):
        locator = (By.CSS_SELECTOR, "div[data-role='additionalDobYear']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def gender_male_option(self):
        locator = (By.CSS_SELECTOR, "div[data-role='Male']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def gender_female_option(self):
        locator = (By.CSS_SELECTOR, "div[data-role='Female']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def gender_other_option(self):
        locator = (By.CSS_SELECTOR, "div[data-role='Other']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def id_input(self):
        locator = (By.CSS_SELECTOR, "input[name='personalId']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def save_btn(self):
        locator = (By.CSS_SELECTOR, "button[data-role='additionalSubmit']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def second_page_validation_error(self):
        locator = (By.CSS_SELECTOR, "div[data-role='validationError']")
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    def select_birth_year(self, year):
        self.birth_year_dropdown.click()
        locator = (By.CSS_SELECTOR, f"div[data-role='dobYearItem{year}']")
        BaseElement(self.driver, by=locator[0], value=locator[1]).click()

    def select_birth_month(self, month):
        self.birth_month_dropdown.click()
        locator = (By.CSS_SELECTOR, f"div[data-role='dobMonthItem{month}']")
        BaseElement(self.driver, by=locator[0], value=locator[1]).click()

    def select_birth_day(self, day):
        self.birth_day_dropdown.click()
        locator = (By.CSS_SELECTOR, f"div[data-role='dobDayItem{day}']")
        BaseElement(self.driver, by=locator[0], value=locator[1]).click()

    def select_birth_date(self, date):
        self.select_birth_day(date.day)
        self.select_birth_month(date.month)
        self.select_birth_year(date.year)

    def go_to_second_registration_page(self, email, password):
        self.email_input.input_text(email)
        self.password_input.input_text(password)
        self.terms_checkbox.click()
        self.sign_up_btn.click()
        self.pin_input.find()

    def fill_second_registration_page(self, pin, phone, first_name, last_name, birth_date, pid, gender='male'):
        self.pin_input.input_text(pin)
        self.phone_input.input_text(phone)
        self.first_name_input.input_text(first_name)
        self.last_name_input.input_text(last_name)
        self.select_birth_date(birth_date)
        self.id_input.input_text(pid)

        if gender == 'male':
            self.gender_male_option.click()
        elif gender == 'female':
            self.gender_female_option.click()
        else:
            self.gender_other_option.click()
