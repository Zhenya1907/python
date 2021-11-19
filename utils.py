import requests

def currency_rates(cur):
    cur = cur.upper()
    txt = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    if cur in txt:
        rub = txt[txt.find('<Value>', txt.find(cur)) : txt.find('</Value>', txt.find(cur))]
        return rub[7:]
    else:
        return None

print(currency_rates('AUD'))