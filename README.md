Hello!!

SnapdMe Automation Tests
1. Prerequisites
Python 3.8+
Chrome browser
ChromeDriver compatible with your Chrome version
Virtual environment (venv recommended)

2. Setup
Clone the repository.
Navigate to the project folder.

3. Create a virtual environment (if not already):
python3 -m venv venv


4. Activate the virtual environment:

source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

5. Install dependencies:
pip install -r requirements.txt


- Folder Structure
 SnapdMe_Automation/
│
├── tests/                  # Test scripts
├── pages/                  # Page Objects
├── resources/              # Test data (images, files, etc.)
├── reports/                # Allure / HTML reports
├── venv/                   # Virtual environment (optional)
├── requirements.txt
└── README.md


6. Running Tests

- To Run all tests:
pytest tests/ -s

- To Run a specific test file:
pytest tests/test_name.py -s


7. Allure Reports

- Generate report (after running tests):
allure generate reports -o allure-report --clean

- Open report in browser:
allure open allure-report

- // Or USe this To print allure Reports write this:
pytest --alluredir=reports/
allure serve reports/


6. Configurations
Update config.yaml for email, password, URLs, or other settings without modifying code.






