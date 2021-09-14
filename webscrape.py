from bs4 import BeautifulSoup
import requests



#html_text = requests.get('https://www.target.com/s?searchTerm=spinach').text
#soup = BeautifulSoup(html_text, 'lxml')
#spinach = soup.find_all('li', class_='Col-favj32-0 iXmsJV h-padding-a-none h-display-flex')

html_text = requests.get('https://www.mlb.com/player/jorge-polanco-593871').text
soup = BeautifulSoup(html_text, 'lxml')
stats = soup.find('div', class_='player-splits__container')
seven_days=''
for i in range(11):
    seven_days += stats.find('th', class_=f'no-sort col-{i}').text.replace('\n','') + ': '
    seven_days += stats.find('td', class_=f'col-{i} row-0').text.replace('\n','') + '\n'


print(seven_days)
