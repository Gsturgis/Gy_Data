import requests
from bs4 import BeautifulSoup
import csv
def scraper():
    url = "https://en.wikipedia.org/wiki/Legality_of_cannabis_by_U.S._jurisdiction#Federal_district"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    table = soup.find("table",{"class":"wikitable sortable"})

    rows = table.findAll("tr")

    data_matrix = []

    #table headers
    columns = [v.text.replace('\n', '') for v in rows[0].findAll("th")]
    #columns.pop(1)
    #columns.pop(5)
    data_matrix.append(columns)
    for i in range(1, len(rows)):
        tds = rows[i].findAll("td")

        if len(tds) == 7:
            values = [tds[0].text.replace('\n','').replace('\xa0', ''), tds[1].text.replace('\n',''),
                      tds[2].text.replace('\n',''), tds[3].text.replace('\n',''),
                      tds[4].text.replace('\n',''), tds[5].text.replace('\n',''), tds[6].text.replace('\n','')]
            data_matrix.append(values)

        else:
            values =[td.text.replace('\n','').replace('\xa0', '') for td in tds]

    with open('Gyasi-Sturgis-cannabis-legality.csv','w') as CSVfile:
        CSVWriter = csv.writer(CSVfile)
        for ml in data_matrix:
            CSVWriter.writerow(ml)


    



if __name__ == '__main__':
    scraper()
   