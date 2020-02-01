from requests import get
from bs4 import BeautifulSoup

ToList = []
seq = []
value = []
check = ["Пойнты", "Название товара", "Название Товара", ""]
url = "https://docs.google.com/spreadsheets/u/0/d/1LzQ574UVm6YKFk05Uyr8LhfF4X8m31PWi_DgNsK4Ly8/htmlview#"
response = get(url)  # response
html = response.text
soup = BeautifulSoup(html, 'html.parser')
parent = soup.find('div', id='sheets-viewport')  # div main body
for i in parent.find_all("td")[1546:]:
    if i.text not in check:
        ToList.append(i.text)
for name in range(0, len(ToList), 2):  # name of item list
    seq.append(ToList[name])
for values in range(1, len(ToList), 2):  # Cost list
    value.append(ToList[values])
cost = dict(zip(seq, value))
print(cost)