import unittest
from selenium import webdriver

from mail.mail import Mail

from pages.registration_page import RegistrationPage
from resources.test_data import TestData


class FirstRegistrationPageTests(unittest.TestCase):

    delete_confirmation_email = False

    def setUp(self):
        if Mail.email_address is None:
            Mail.generate_email_address()

        self.browser = webdriver.Chrome()
        self.registration_page = RegistrationPage(driver=self.browser)
        self.registration_page.go()

    def test_first_registration_page_submission(self):

        self.delete_confirmation_email = True

        self.registration_page.email_input.input_text(Mail.email_address)
        self.assertEqual(self.registration_page.email_input.attribute('value'), Mail.email_address,
                         'Email field was not populated with test data.')

        self.registration_page.password_input.input_text(TestData.password)
        self.assertEqual(self.registration_page.password_input.attribute('value'), TestData.password,
                         'Password field was not populated with test data.')

        self.registration_page.terms_checkbox.click()
        self.registration_page.sign_up_btn.click()

        self.assertTrue(Mail.get_registration_pin())
        self.assertTrue(self.registration_page.pin_input.find(), 'Second page of registration form is not opened,')

    def test_email_validation_ignore_side_spaces(self):

        self.delete_confirmation_email = True

        self.registration_page.email_input.input_text(f'  {Mail.email_address}   ')
        self.assertFalse(self.registration_page.email_error.find())

        self.registration_page.password_input.input_text(TestData.password)
        self.registration_page.terms_checkbox.click()
        self.registration_page.sign_up_btn.click()

        self.assertTrue(Mail.get_registration_pin())
        self.assertTrue(self.registration_page.pin_input.find(), 'Second page of registration form is not opened,')

    def test_email_validation_empty_field(self):

        self.delete_confirmation_email = False

        self.registration_page.email_input.click()
        self.registration_page.password_input.click()

        self.assertTrue(self.registration_page.email_error.find())
        self.assertEqual(self.registration_page.email_error.text(), 'Email is required')

    def test_email_validation_missing_at(self):

        self.delete_confirmation_email = False

        self.registration_page.email_input.input_text('testemailyopmail.com')
        self.registration_page.password_input.click()

        self.assertTrue(self.registration_page.email_error.find())
        self.assertEqual(self.registration_page.email_error.text(), 'Please enter a valid email')

    def test_password_validation_empty_field(self):

        self.delete_confirmation_email = False

        self.registration_page.email_input.input_text(Mail.email_address)
        self.registration_page.password_input.click()
        self.registration_page.email_input.click()

        self.assertTrue(self.registration_page.password_error.find())
        self.assertEqual(self.registration_page.password_error.text(), 'Password is required')

    def test_promocode_field_appearance(self):

        self.delete_confirmation_email = False

        self.registration_page.promocode_question.click()
        self.assertTrue(self.registration_page.promocode_input.find())

        self.registration_page.close_promocode_icon.click()
        self.assertFalse(self.registration_page.promocode_input.find())

    def test_redirect_to_login_page(self):

        self.delete_confirmation_email = False

        self.registration_page.login_link.click()
        self.assertEqual(self.browser.current_url, 'https://www.optibet.lv/en/login')

    def tearDown(self):
        if self.delete_confirmation_email:
            Mail.delete_confirmation_message()
        self.browser.quit()
