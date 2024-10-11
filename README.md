# Python Automation Framework for orangehrmlive website
This is a project for a web automation framework using Selenium, Pytest, Python, allure reports and page object model. This automates the Site https://opensource-demo.orangehrmlive.com .

# How to install it
* Make sure you have python installed on your machine by typing in console "python --version"
  ```sh
   https://realpython.com/installing-python/#step-1-download-the-python-3-installer.
  ```
* Note: It is recommended to create a Python virtual environment to keep dependencies organized
  ```sh
    python -m venv venv
    source venv/bin/activate
  
* If you wish to clone without env folder you have to download following python packages by running following pip commands:
  ```sh
    ^ pip install selenium (for webdriver)
    ^ pip install pytest (for pytest framework)
    ^ pip install pytest-html (for pytest html report)
    ^ pip install allure-pytest (for allure reporting)
  
* HTML Reporting:
  ```sh
    --html=reports/report1.html  # For Pytest HTML reporting
    --self-contained-html
  ```

* Allure Reporting:
  ```sh
    --alluredir=<path>   
  ```
* Generating Allure Reports
  To generate and serve Allure reports, execute the following command in the project path:
  ```sh
    ^ allure serve <path where allure files are>
  
* To run your tests and generate Allure reports, use the following command:
  you have to install allure command line for this and add the allure folder installation into system environment variable
  ```sh
    ^ python -m pytest --alluredir=reports/allure-reports --browser=chrome
     
* Technologies used
  ```sh
     1. Python 3.
     2. Selenium Package.
     3. Pytest in order to have test cases, init and tear down.
