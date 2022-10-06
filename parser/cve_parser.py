import requests as r
from bs4 import BeautifulSoup


def parser(keywords: list) -> list:
    result = []
    for keyword in keywords:
        res = r.get(f'https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword={keyword}')
        soup = BeautifulSoup(res.text, 'html.parser')
        table = soup.find('div', {"id": "TableWithRules"})
        cve_list = []
        cves = table.find_all('td')
        cve = [cves[0].text, cves[1].text]
        cve_list.append(cve)
        result.append(cve_list)
    return result

