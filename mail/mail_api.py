import json
import inspect
import requests
from pprint import pprint

from resources.test_data import TestData


class MailApi:

    def __init__(self):

        self.base = "https://mailsac.com"
        base_dict = {
            'content-type': 'application/json',
            'Mailsac-Key': TestData.mailsac_key,
        }
        self.inpType = base_dict
        self.timeout = 30

    def logCall(self, response, _url):

        pprint(f"Response_code == <{response.status_code}> / url <{_url}>")

    def getRest(self, _url, getName):

        response = requests.get(_url, headers=self.inpType, timeout=self.timeout)
        self.logCall(response, _url)

        response_content = None

        try:
            response_content = json.loads(response.content)

        except Exception as e:
            print(f"Possible issue with json returned in {getName} call. {e}")

        return response, response_content

    def deleteRest(self, _url, deleteName):

        response = requests.delete(_url, data=None, headers=self.inpType, timeout=self.timeout)
        self.logCall(response, _url)

        response_content = None

        try:
            response_content = json.loads(response.content)

        except Exception as e:
            print(f"Possible issue with json returned in {deleteName} call. {e}")

        return response, response_content

    def getInboxEmails(self, email_address):
        _url = self.base + f'/api/addresses/{email_address}/messages'
        return self.getRest(_url, format(inspect.currentframe().f_code.co_name))

    def deleteMessageById(self, email_address, message_id):
        _url = self.base + f'/api/addresses/{email_address}/messages/{message_id}'
        return self.deleteRest(_url, format(inspect.currentframe().f_code.co_name))
