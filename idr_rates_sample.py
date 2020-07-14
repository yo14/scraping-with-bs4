import requests

# json_data = requests.get('http://www.floatrates.com/daily/idr.json')

json_data = {'usd': {'code': 'USD', 'alphaCode': 'USD', 'numericCode': '840', 'name': 'U.S. Dollar', 'rate': 6.9338562803874e-05, 'date': 'Tue, 14 Jul 2020 12:00:02 GMT', 'inverseRate': 14421.98914374}, 'eur': {'code': 'EUR', 'alphaCode': 'EUR', 'numericCode': '978', 'name': 'Euro', 'rate': 6.114372971987e-05, 'date': 'Tue, 14 Jul 2020 12:00:02 GMT', 'inverseRate': 16354.906784089}}

for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])

