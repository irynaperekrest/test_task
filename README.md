#### Tests location

Tests are located in ```/tests``` and split in classes:  
- ```test_1_first_reg_page.py``` contains tests for first page of registration form
- ```test_2_second_reg_page.py``` contains tests for second page of registration form
- ```test_3_game_search.py``` contains tests for game search

Separation is done based on tested object and setup/teardown steps that tests in each class require.  

Test scenarios that are not automated (due to lack of time), but should also be tested:  
- registration page design (list of elements, text)
- more input fields validation tests (e.g. email does't contain domain name or account name, data too short or too long, includes unsupported symbols)
- dropdown validation tests (can't select date that doesn't exist, like 30.02)

#### Tests execution

Before executing test it's important to fill in your mail service API key and desired log file location in ```/resources/test_data.py```  
  
To execute tests from specific class - run code from that class.  
To execute all tests - run code from ```/tests/test_suite.py```  
To execute selected tests from one/several class - form test suite in ```/tests/test_suite.py``` and run it (example is commented out in test_suite.py)  

#### Page objects  

I used page objects pattern for this framework. I see it as an elegant solution for web testing.  
Implementation - ```/pages```

#### Mail server  

To receive registration PIN and complete registration I used disposable testing email inbox service ```https://mailsac.com/```  
It provides open API to work with messages in inbox.  
I use it to receive confirmation message to randomly generated address and fetch PIN from its title.
Then I delete message not to have expired PIN stored there in case I use same email address again. 
Implementation is in ```/mail```

#### Logging

In current implementation it's not really informative. Normally I would try to log most of the test steps to simplify debugging in case of fails.  
Now it's just an initialization (in test_suite.py) and reminder for myself that it should be added.  

#### Test data

Test data for testing (mostly hardcoded in this case) is stored in ```/resources/test_data.py``` 