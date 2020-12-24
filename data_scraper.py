import requests
from capital_code_hash import capital_codes
frequency = ['D','W', 'M', 'Q', 'Y'] #Day, week, month, quarter, year
capital_code = capital_codes['ADBL']
desired_frequency = 'D'
base_url = f"http://www.nepalstock.com/company/graphdata/{capital_code}/{desired_frequency}"
response = requests.get(base_url)
print(response.json())