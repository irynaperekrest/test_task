import datetime
from dateutil.relativedelta import relativedelta


class TestData:

    # Register at https://mailsac.com/ (free account).
    # Create API key at https://mailsac.com/api-keys
    mailsac_key = 'Please insert your data'

    # Any location on your machine
    log_file_location = 'Please insert your data'

    existing_acc_email = 'testtask@yopmail.com'
    password = "TestTask10!"

    phone = 55511111
    first_name = 'John'
    last_name = 'Doe'
    birth_date = datetime.date(1910, 1, 1)

    pid_not_matching_birth_date = '050510-12643'

    # For one successful run only
    pid_matching_birth_date = '010110-11480'

    game_name = 'BOOSTER'

    @staticmethod
    def get_latest_valid_birth_date():

        return datetime.date.today() - relativedelta(years=18)

    @staticmethod
    def get_invalid_birth_date():

        return TestData.get_latest_valid_birth_date() + relativedelta(days=1)
