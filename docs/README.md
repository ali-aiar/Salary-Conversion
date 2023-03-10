# Salary Conversion
The salary conversion app is a tool that converts salary data from a JSON database that is connected to the user's JSON placeholder to the desired currency.
## Getting Started
### Prerequisites
What things do you need to install the software and how to install them
1. Python 3.6 or higher
2. If you are in windows, there is a chance to get an error because of the execution policy. If you get the error, run this program as an administrator
```console
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
```
### Installation
1. Clone this repository
```bash
git clone https://github.com/ali-aiar/Salary-Conversion.git
```
2. Go to the main directory 
```bash
cd Salary-Conversion
```
3. Create a virtual environment 
```bash
python -m venv venv
```
4. Activate the virtual environment
```bash
source venv/bin/activate  # Linux or macOS
.\venv\Scripts\activate  # Windows
```
5. Install the required packages by running the following command:
```bash
pip install -r requirements.txt
```
6. Create a .env file inside ./ or main directory, in this case for users and exchange rates API
```code
USER_DATA_API = 'http://jsonplaceholder.typicode.com/users'
EXCHANGE_RATE_API_KEY = 'your api key'
EXCHANGE_RATE_API_URL = 'https://api.apilayer.com/exchangerates_data/latest'
```   
7. Run the program by executing the following command:
```bash
python main.py
```
8. To deactivate the virtual environment, run:
```bash
deactivate
```
## Running the tests
To run the test you must be in the ./ or main directory. 
### Test the models
The test will use unittest library, to know if the model working as intended from the salary model to the user model.
```bash
python -m unittest ./tests/test_models.py
```
### Test the services
The services use to get currency rates using API, test for to get currency rates and conversion.
```bash
python -m unittest ./tests/test_services.py
```
### Test the controllers
The controllers use to manage the flow of data between models, services, and views. 
```bash
python -m unittest ./tests/test_controllers.py
```