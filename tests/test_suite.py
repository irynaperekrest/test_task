import logging
import unittest
from resources.test_data import TestData

from tests.test_1_first_reg_page import FirstRegistrationPageTests
from tests.test_2_second_reg_page import SecondRegistrationPageTests
from tests.test_3_game_search import GameSearchTests

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=f'{TestData.log_file_location}/testtask.log', filemode='w')

# To run selected tested from several test classes, uncomment this part and add tests to test suite
#
# def suite():
#     test_suite = unittest.TestSuite()
#     test_suite.addTest(FirstRegistrationPageTests('test_email_validation_empty_field'))
#     test_suite.addTest(SecondRegistrationPageTests('test_birth_date_pid_correlation'))
#     test_suite.addTest(GameSearchTests('test_booster_search'))
#
#     return test_suite
#
#
# unittest.TextTestRunner().run(suite())

# Comment out this part to run only tests in test suite
if __name__ == "__main__":
    unittest.main()
