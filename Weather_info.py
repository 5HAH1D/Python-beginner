import requests
from bs4 import BeautifulSoup

make_req = requests.get('https://weather.com/en-PK/weather/today/l/8b7fc201ff30b687ec10b5a5df4528dd8adfd7a35b00fcabd4719f14c5a4bd4e')
labels_list = []
labels_data_list = []
combined_data = {}
soup = BeautifulSoup(make_req.content, features='lxml')
header = soup.find('div', class_='CurrentConditions--header--27uOE').text
current_condition = soup.find('span', class_='CurrentConditions--tempValue--3a50n').text
today = soup.find('div', class_='CurrentConditions--tempHiLoValue--3SUHy').text
today1 = soup.find('div', class_='CurrentConditions--phraseValue--2Z18W').text
feels_like = soup.find('div', class_='TodayDetailsCard--feelsLikeTemp--3fwAJ').get_text(separator=' ')
details = soup.find('div', class_='TodayDetailsCard--detailsContainer--16Hg0')
for data in details:
    labels = soup.find_all('div', class_='WeatherDetailsListItem--label--3PkXl')
    for label in labels:
        labels_list.append(label.text)
    labels_data = soup.find_all('div', class_='WeatherDetailsListItem--wxData--2s6HT')
    for label_data in labels_data:
        labels_data_list.append(label_data.text)

for key, value in zip(labels_list, labels_data_list):
    combined_data[key] = value
print(f"\n{header}\n{current_condition}\t{today1}\n({today})\n{feels_like}\n")
for keys, values in combined_data.items():
    print(f"{keys}\t{values}")
