## Deck of Cards API testing framework using Python
    The framework covers a total of 8 test cases for two endpoints. 
    It is built utilizing OOP principles with scalability in mind. 

### Folder structure

    config
        config.properties
    helper
        test_data.json
        utils.py
    reports
        report.html
    tests
        test_base.py
        test_deck.py
        test_drawcards.py
    requirements.txt

### Technology used:
    Framework: PyTest

    Libraries: requests, configparser, json, pytest-html, os
        
    
### Setup and run (Windows):
    1. Install Python 3 and update PATH system variable
    2. Clone the repository
    3. Run setup.bat (creates virtual environment and installs required packages)
    4. Run run-tests.bat


### View html report

    Open reports\report.html file in browser