import logging
import random
import re
import string
import time

from mail.mail_api import MailApi

logger = logging.getLogger('mail')


class Mail:

    email_address = None
    message_id = None
    registration_pin = None

    @staticmethod
    def generate_email_address():
        length = 10
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length)).lower()
        Mail.email_address = f'{random_string}@mailsac.com'

    @staticmethod
    def wait_for_confirmation_message():

        root = MailApi()

        for check in range(15):

            code, messages_list = root.getInboxEmails(Mail.email_address)

            for message in messages_list:

                try:

                    if message['from'][0]['name'] == 'Optibet':
                        Mail.message_id = message['_id']
                        return message['subject']

                except Exception as e:
                    logger.error(f'Problem accessing email data. {e}')

            time.sleep(4)

    @staticmethod
    def get_registration_pin():

        email_subject = Mail.wait_for_confirmation_message()

        try:
            Mail.registration_pin = int(re.search(r'[0-9]{4}', email_subject).group())
            return True
        except Exception as e:
            logger.error(f'Could not get registration Pin from email {Mail.email_address}. {e}.')

    @staticmethod
    def delete_confirmation_message():

        root = MailApi()
        root.deleteMessageById(Mail.email_address, Mail.message_id)
