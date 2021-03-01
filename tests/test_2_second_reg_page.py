import unittest
from selenium import webdriver

from mail.mail import Mail
from pages.registration_page import RegistrationPage
from resources.test_data import TestData


class SecondRegistrationPageTests(unittest.TestCase):

    def setUp(self):
        if Mail.email_address is None:
            Mail.generate_email_address()

        self.browser = webdriver.Chrome()
        self.registration_page = RegistrationPage(driver=self.browser)
        self.registration_page.go()
        self.registration_page.go_to_second_registration_page(Mail.email_address, TestData.password)
        Mail.get_registration_pin()

    def test_age_less_18_not_acceptable(self):

        # I created this test assuming people under 18 should not be able to complete registration.
        # They should not even be able to select their birth date.
        # However, birth dates for people who have 18th birthday later this year are available in the form.
        # Looks like a bug to me.
        # Not sure what would be the best way to handle such cases (display error, don't have such dates available etc.)
        # In this test I'm expecting an error under the selected date.

        date = TestData.get_invalid_birth_date()
        self.registration_page.select_birth_date(date)
        self.registration_page.id_input.click()

        self.assertTrue(self.registration_page.second_page_validation_error.find())

    def test_birth_date_pid_correlation(self):

        self.registration_page.fill_second_registration_page(
            pin=Mail.registration_pin,
            phone=TestData.phone,
            first_name=TestData.first_name,
            last_name=TestData.last_name,
            birth_date=TestData.birth_date,
            pid=TestData.pid_not_matching_birth_date,
        )

        self.registration_page.save_btn.click()

        self.assertTrue(self.registration_page.second_page_validation_error.find())
        self.assertEqual(self.registration_page.second_page_validation_error.text(),
                         'Date of birth does not match with personal ID')

    def test_changing_email(self):

        self.registration_page.change_email_link.click()

        self.assertTrue(self.registration_page.email_input.find())

    def test_second_registration_page_successful_submission(self):

        self.registration_page.fill_second_registration_page(
            pin=Mail.registration_pin,
            phone=TestData.phone,
            first_name=TestData.first_name,
            last_name=TestData.last_name,
            birth_date=TestData.birth_date,
            pid=TestData.pid_matching_birth_date,
        )

        self.registration_page.save_btn.click()
        self.assertEqual(self.browser.current_url, 'https://www.optibet.lv/en/account/profile?dialogType=set-limit')

    def tearDown(self):
        Mail.delete_confirmation_message()
        self.browser.quit()
